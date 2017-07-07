#ifndef _DEEPCAPTURE_H_
#define _DEEPCAPTURE_H_

class DeepCapture
{
public:
  DeepCapture();
  ~DeepCapture();

  virtual void init();
  virtual void start();
  virtual void stop();
};

#endif
