/*
  Objetos de para la produccion y determinacion de escenas
   - Luces
   - Camaras
*/

/* Camara */
class Camera { 
  public:
    Vector3 position;
    int width, height;
    float invWidth, invHeight;
    float fov, aspectratio, angle;
    float angleX, angleY, angleZ;

    Camera(Vector3 _position, int _width, int _height, float _fov) { 
      position = _position;
      width = _width;
      height = _height;
      invWidth = 1 / (float)width;
      invHeight = 1 / (float)height;
      fov = _fov;
      aspectratio = width / float(height);
      angle = tan(0.5 * fov * M_PI/ 180.0);
      angleX = 0;
      angleY = 0;
      angleZ = 0;
    }

    Vector3 pixelToViewport(Vector3 pixel) {
      float vx = (2 * ((pixel.x + 0.5) * invWidth) - 1) * angle * aspectratio;
      float vy = (1 - 2 * ((pixel.y + 0.5) * invHeight)) * angle;
      Vector3 rayDirection  = Vector3(vx, vy, pixel.z);
      rayDirection.rotateX(angleX);
      rayDirection.rotateY(angleY);
      rayDirection.rotateZ(angleZ);
      rayDirection.normalize();
      return rayDirection;
    }
};

/* Luces */
class Light {
  public:
    Vector3 position;
    Vector3 intensity;
    unsigned char type;

    int samples;
    float width, height;

    Light() : position(Vector3()), intensity(Vector3()) { type = 0x01; }
    Light(Vector3 _intensity) : position(Vector3()), intensity(_intensity) { type = 0x01; } 
    Light(Vector3 _position, Vector3 _intensity) : position(_position), intensity(_intensity) { type = 0x01; } 
    virtual float attenuate(const float &r) const { return 1.0; }
};

class AmbientLight : public Light {
  public:
    AmbientLight() : Light() { type = 0x02; }
    AmbientLight(Vector3 _intensity) : Light(_intensity) { type = 0x02; }
    float attenuate(const float &r) const { return 1.0; }
};

class DirectionalLight : public Light {
  public:
    DirectionalLight() : Light() { type = 0x04; }
    DirectionalLight(Vector3 _position, Vector3 _intensity) : Light(_position, _intensity) { type = 0x04; }
    float attenuate(const float &r) const { return 1.0; }
};

class PointLight : public Light {
  public:
    PointLight() : Light() { type = 0x08; }
    PointLight(Vector3 _position, Vector3 _intensity) : Light(_position, _intensity) { type = 0x08; }
    float attenuate(const float &r) const { return 1.0 / (r * r); }
};

class SpotLight : public Light {
  public:
    SpotLight() : Light() { type = 0x10; }
    SpotLight(Vector3 _position, Vector3 _intensity) : Light(_position, _intensity) { type = 0x10; }
    float attenuate(Vector3 Vobj, Vector3 Vlight) const { return Vobj.dot(Vlight); }
};

class AreaLight : public Light {
  public:
    AreaLight() : Light() {
      type = 0x20;
      samples = 2;
      width = 4;
      height = 4;
    }
    AreaLight(Vector3 _position, Vector3 _intensity) : Light(_position, _intensity) {
      type = 0x20;
      samples = 2;
      width = 4;
      height = 4;
    }
    float attenuate(const float &r) const { return 1.0; }
};