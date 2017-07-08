%module deep_capture

%{
#define SWIG_FILE_WITH_INIT
%}

%include "numpy.i"
%include "stdint.i"

%init %{
import_array();
%}

%{
#include "PixelBuffer.h"
#include "DeepCapture.h"
%}

%include "PixelBuffer.h"
%include "DeepCapture.h"

%apply (int DIM1, uint8_t* ARGOUT_ARRAY1) {(int size, uint8_t *arr)};
%inline %{
void to_numpy(uint8_t* buffer, int size, uint8_t *arr){
  memcpy(arr, buffer, size);
}
%}
