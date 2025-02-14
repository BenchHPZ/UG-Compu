#ifndef CS488_MATERIAL_H
#define CS488_MATERIAL_H

#include "algebra.h"

class Material {
public:
  virtual ~Material();
  virtual void apply_gl() const = 0;

protected:
  Material()
  {
  }
};

class PhongMaterial : public Material {
public:
  PhongMaterial(const Colour& kd, const Colour& ks, double shininess);
  virtual ~PhongMaterial();

  virtual void apply_gl() const;

private:
  Colour m_kd;
  Colour m_ks;

  double m_shininess;
};


#endif
