using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;

using Microsoft.Kinect;

namespace Doorbell
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        KinectSensor sensor;
        ColorFrameReader reader;
        public MainWindow()
        {
            InitializeComponent();
            this.Loaded += OnLoaded;
        }

        private void OnLoaded(object sender, RoutedEventArgs e)
        {
            this.sensor = KinectSensor.GetDefault();
            this.sensor.Open();

            this.reader = this.sensor.ColorFrameSource.OpenReader;
            this.reader.FrameArrived += OnFrameArrived;
        }

        private void OnFrameArrived(object sender, ColorFrameArrivedEventArgs e)
        {
            using (var frame = e.FrameReference.AcquireFrame()) {
                if (frame != null) {
                    camera.Source = ProcessFrame(frame)
                }
            }
        }

        private ImageSource ProcessFrame(ColorFrame frame)
        {
            throw new NotImplementedException();
        }
    }
}
