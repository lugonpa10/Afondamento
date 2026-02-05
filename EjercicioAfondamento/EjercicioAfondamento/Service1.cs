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
        
            ServidorFechaHora servidor = new ServidorFechaHora();

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



        protected override void OnStart(string[] args)
        {
            servidor.WriteEvent("Iniciando el servidor");
            Thread hilo = new Thread(() => servidor.initServer());
            hilo.IsBackground = true;
            hilo.Start();
        }

        protected override void OnStop()
        {
            servidor.WriteEvent("Deteniendo el servidor");
            servidor.StopServer();

        }

    }

}

