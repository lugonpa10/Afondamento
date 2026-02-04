using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Diagnostics;
using System.IO;
using System.Linq;
using System.Net;
using System.Net.Sockets;
using System.ServiceProcess;
using System.Text;
using System.Threading;
using System.Threading.Tasks;

namespace EjercicioAfondamento
{
    public partial class ServidorAfondamento : ServiceBase
    {
        public bool ServerRunning { set; get; } = true;
        public int Port { set; get; } = 31416;
        private int puertoDefecto = 31416;

        public bool puertoOcupado = true;
        private Socket s;

        public ServidorAfondamento()
        {
            InitializeComponent();
            string nombre = "ServidorAfondamento";
            string logDestino = "Application";
            if (!EventLog.SourceExists(nombre))
            {
                EventLog.CreateEventSource(nombre, logDestino);
            }
        }

        public void WriteEvent(string mensaje)
        {
            const string nombre = "ServidorAfondamento";
            try
            {
                EventLog.WriteEntry(nombre, mensaje);

            }
            catch (Exception)
            {
                string mensajeError = $"[ERROR]{DateTime.Now.ToString("G")}";
                guardarComandos(mensajeError);
            }
        }

        protected override void OnStart(string[] args)
        {
            WriteEvent("Iniciando el servidor");
            Thread hilo = new Thread(initServer);
            hilo.IsBackground = true;
            hilo.Start();
        }

        protected override void OnStop()
        {
            WriteEvent("Deteniendo el servidor");
            ServerRunning = false;

        }



        public void initServer()
        {

            Port = leerPuerto();
            IPEndPoint ie = new IPEndPoint(IPAddress.Any, Port);
            s = new Socket(AddressFamily.InterNetwork, SocketType.Stream, ProtocolType.Tcp);

            try
            {
                s.Bind(ie);
                s.Listen(10);
                WriteEvent($"Puerto {ie.Port} libre");



                while (ServerRunning)
                {
                    Socket client = s.Accept();
                    Thread hilo = new Thread(() => ClientDispatcher(client));
                    hilo.IsBackground = true;
                    hilo.Start();


                }

            }
            catch (SocketException e) when (e.ErrorCode == 10048)
            {
                WriteEvent($"El puerto {Port} esta ocupado");
                try
                {
                    s = new Socket(AddressFamily.InterNetwork, SocketType.Stream, ProtocolType.Tcp);
                    ie = new IPEndPoint(IPAddress.Any, puertoDefecto);
                    s.Bind(ie);
                    s.Listen(10);
                    WriteEvent($"El puerto por defecto {puertoDefecto} esta libre");

                    while (ServerRunning)
                    {
                        Socket client = s.Accept();
                        Thread hilo = new Thread(() => ClientDispatcher(client));
                        hilo.IsBackground = true;
                        hilo.Start();


                    }



                }
                catch (SocketException e2) when (e2.ErrorCode == 10048)
                {
                    WriteEvent($"Todos los puertos asignados estan ocupados");
                    StopServer();


                }

            }
            catch (SocketException)
            {

                Console.WriteLine("Fin del servidor");

            }

        }
        private void ClientDispatcher(Socket sClient)
        {
            using (sClient)
            {
                IPEndPoint ieClient = (IPEndPoint)sClient.RemoteEndPoint;
                Console.WriteLine($"Cliente conectado: {ieClient.Address}" +
                    $" en puerto {ieClient.Port}");

                Encoding codificacion = Console.OutputEncoding;
                using (NetworkStream ns = new NetworkStream(sClient))
                using (StreamWriter sw = new StreamWriter(ns))
                using (StreamReader sr = new StreamReader(ns))
                {
                    sw.AutoFlush = true;

                    string opcion = "";
                    sw.WriteLine("Bienvenido a mi servidor,introduce un comando");
                    {
                        try
                        {
                            opcion = sr.ReadLine();
                            if (opcion != null)
                            {
                                string formato = $"[{DateTime.Now.ToString("G")}-@{ieClient.Address}] {opcion}";
                                guardarComandos(formato);

                                if (opcion != "time" && opcion != "date" && opcion != "all")
                                {
                                    sw.WriteLine("El comando no es valido");
                                }
                                else
                                {
                                    switch (opcion)
                                    {
                                        case "time":
                                            sw.WriteLine(DateTime.Now.ToString("T"));

                                            break;
                                        case "date":
                                            sw.WriteLine(DateTime.Now.ToString("d"));

                                            break;

                                        case "all":
                                            sw.WriteLine(DateTime.Now.ToString("G"));

                                            break;
                                    }

                                }
                            }
                        }

                        catch (IOException)
                        {
                            opcion = null;
                        }

                    }
                }
            }
        }


        public void StopServer()
        {
            Console.WriteLine("Deteniendo servidor");
            ServerRunning = false;
            s.Close();

        }

        public int leerPuerto()
        {
            string programdata = Environment.GetEnvironmentVariable("programdata");
            string archivo = "puertos.txt";
            string rutaArchivo = programdata + "\\" + archivo;
            int puertoDefecto = 31416;
            int puertoMaximo = IPEndPoint.MaxPort;
            try
            {
                string linea = "";
                using (StreamReader sr = new StreamReader(rutaArchivo))
                {
                    linea = sr.ReadLine()?.Trim();
                    if (linea != null && int.TryParse(linea, out int puerto))
                    {
                        if (puerto > puertoMaximo || puerto < 0)
                        {
                            WriteEvent("Puerto no valido");
                            return puertoDefecto;
                        }
                        else
                        {
                            WriteEvent($"El puerto {puerto} esta libre ");
                            return puerto;
                        }
                    }
                    else
                    {
                        WriteEvent("Ocurrio un error con el archivo");
                        return puertoDefecto;
                    }


                }




            }
            catch (FileNotFoundException e)
            {
                WriteEvent($"No se encontro el archivo: {e}");
                return puertoDefecto;
            }
            catch (IOException e)
            {
                WriteEvent($"Error en el archivo: {e}");
                return puertoDefecto;
            }
        }

        public void guardarComandos(string mensaje)
        {
            string programData = Environment.GetEnvironmentVariable("programdata");
            string archivo = "log.txt";
            string rutaArchivo = programData + "\\" + archivo;
            try
            {
                using (StreamWriter sw = new StreamWriter(rutaArchivo,true))
                {
                    sw.WriteLine(mensaje);
                }
            }
            catch (Exception)
            {

            }
        }

    }
}

