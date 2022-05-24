#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <tensorflow/c/c_api.h>
#include "Clasificar.h"

// Definir funciones
int Okay(TF_Status* status);


int Okay(TF_Status* status) {
    if (TF_GetCode(status) != TF_OK) {
        fprintf(stderr, "ERROR: %s\n", TF_Message(status));
        return 0;
    }
    return 1;
}


int EstadoJugador(float **imagen) {
    float respuesta=0;
    int posicion = 0;
    TF_Graph* Graph = TF_NewGraph();
    TF_Status* Status = TF_NewStatus();
    TF_SessionOptions* SessionOpts = TF_NewSessionOptions();
    TF_Buffer* RunOpts = NULL;

    const char* saved_model_dir = "D:\\Proyectos\\Pruebas\\resultado 4\\convert2";
    const char* tags = "serve";
    int ntags = 1;
    printf("iniciando tensores: %s\n", TF_Version());

    TF_Session* Session = TF_LoadSessionFromSavedModel(SessionOpts, RunOpts, saved_model_dir, &tags, ntags, Graph, NULL, Status);

    int NumInputs = 1;
    TF_Output* Input = (TF_Output*)malloc(sizeof(TF_Output) * NumInputs);
    TF_Output x = { TF_GraphOperationByName(Graph, "serving_default_conv2d_1_input"), 0 };
    Input[0] = x;

    int NumOutputs = 1;
    TF_Output* OutPut = (TF_Output*)malloc(sizeof(TF_Output) * NumOutputs);
    TF_Output y = { TF_GraphOperationByName(Graph, "StatefulPartitionedCall"), 0 };
    OutPut[0] = y;

    TF_Tensor** InputValues = (TF_Tensor**)malloc(sizeof(TF_Tensor*) * NumInputs);
    TF_Tensor** OutputValues = (TF_Tensor**)malloc(sizeof(TF_Tensor*) * NumInputs);

    int i;
    int ndims = 4;//2
    int size;
    int64_t input_dims[] = { 1, 150, 150, 1 };
    float *input_data = *imagen; //Debe ir la imagen como array

    TF_Tensor* input_tensor = TF_AllocateTensor(TF_FLOAT, input_dims, ndims, sizeof(float) * 150 * 150);
    size = TF_TensorByteSize(input_tensor);
    float* tensor_buffer = (float*)TF_TensorData(input_tensor);
    memcpy(tensor_buffer, input_data, size);

    InputValues[0] = input_tensor;
    OutputValues[0] = { NULL };

    TF_SessionRun(Session, NULL, Input, InputValues, NumInputs, OutPut, OutputValues, NumOutputs, NULL, 0, NULL, Status);

    if (Okay(Status))
    {
        int nbytes = sizeof(float) * 4;
        if (TF_TensorByteSize(OutputValues[0]) != nbytes) {
            fprintf(stderr,
                "ERROR: Expected predictions tensor to have %zu bytes, has %zu\n",
                nbytes, TF_TensorByteSize(OutputValues[0]));
            TF_DeleteTensor(OutputValues[0]);
            return 0;
        }
        float* predictions = (float*)malloc(nbytes);
        memcpy(predictions, TF_TensorData(OutputValues[0]), nbytes);
        TF_DeleteTensor(OutputValues[0]);

        printf("Predictions:\n");
        for (int i = 0; i < 4; ++i) {
            printf("\tpredicted y = %f\n", predictions[i]);
            if (i == 0) {
                respuesta = predictions[i];
                posicion = 0;
            }
            else {
                if (respuesta < predictions[i]) {
                    respuesta = predictions[i];
                    posicion = i;
                }
            }
        }
        free(predictions);
    }

    TF_DeleteGraph(Graph);
    TF_DeleteSession(Session, Status);
    TF_DeleteSessionOptions(SessionOpts);
    TF_DeleteStatus(Status);
    return posicion;
}
