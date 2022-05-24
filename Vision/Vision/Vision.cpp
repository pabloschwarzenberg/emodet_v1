#include <iostream>
#include <ctime>
#include <stdlib.h>
#include <opencv2/opencv.hpp>
#include <opencv2/imgproc/imgproc.hpp>
#include "Clasificar.h"

using namespace std;
using namespace cv;

//Definir funciones
int CapturarCara();


int CapturarCara() {
    int k = 0;
    int prediccion = 0;

    //Variable guarda pixel
    float pixel;
    float *imagen;
    imagen = (float*)malloc(sizeof(float) * 22500);

    //configuracion OpenCV
    VideoCapture cap;
    Mat frame;
    cap >> frame;

    Mat MyData;
    int width;
    int height;

    if (!cap.open(0)) {
        return 0;
    }
    else {
        cap.read(frame);
        resize(frame, frame, Size(), 0.235, 0.313);


        //MyData = (float *)frame.data;
        frame.convertTo(MyData, CV_32F);
        //float* data = MyData.ptr<float>();
        cv::cvtColor(frame, frame, cv::COLOR_BGR2GRAY);
        imwrite("photo.jpg", frame);


        width = frame.cols;
        height = frame.rows;
        //cout << data << endl;
        //cout << format(frame, "C"   );
        //EstadoJugador(data);
        format(frame, Formatter::FMT_C);

        for (int i = 0; i < height; i++)
        {
            for (int j = 0; j < width; j++)
            {
                pixel = frame.at<uchar>(i, j)/255;
                imagen[k] = pixel;
                k += 1;
            }
        }
    }
    prediccion = EstadoJugador(&imagen);

    if (prediccion == 0) {
        cout << "Aburrimiento-Neutro" << endl;
    }
    else if (prediccion == 1) {
        cout << "Alegria-Felicidad" << endl;
    }
    else if (prediccion == 2) {
        cout << "Ansiedad-Frustracion-Molestia" << endl;
    }
    else {
        cout << "Sorpresa" << endl;
    }
}


int main() {

    unsigned t_start, t_moment;

    t_start = clock() / CLOCKS_PER_SEC;

    for (;;) {
        t_moment = clock() / CLOCKS_PER_SEC;


        if ((t_moment - t_start) % 15 == 0)
        {
            CapturarCara();
        }

    }

    return 0;
}
