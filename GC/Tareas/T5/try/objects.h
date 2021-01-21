/*
  Objetos para que configurar y simular el 
  rendering y para posucionar en la escena.
*/


/*  Rayo  */
class Ray {
  public:
    Vector3 origin;
    Vector3 direction;
    Ray(Vector3 _origin, Vector3 _direction) : origin(_origin), direction(_direction) {}
};


/*  Figuras para trabajar.  */
class Shape {
  public:
    Vector3 center;           // Position
    Color color;              // Surface Diffuse Color
    Color color_specular;     // Surface Specular Color
    float ka, kd, ks;         // Ambient, Diffuse, Specular Coefficents
    float shininess;
    float reflectivity;       // Reflectivity of material [0, 1]
    float transparency;       // Transparency of material [0, 1]
    float glossiness;         // Strength of glossy reflections
    float glossy_transparency; // Strength of glossy transparency

    virtual bool intersect(const Ray &ray, float &to, float &t1) { return false; }
    virtual Vector3 getNormal(const Vector3 &hitPoint) { return Vector3(); }
};

class Sphere : public Shape {
  public:
    float radius, radius2;

    Sphere(
      const Vector3 &_center, const float _radius, const Color &_color, 
      const float _ka, const float _kd, const float _ks, const float _shinny = 128.0, 
      const float _reflectScale = 1.0, const float _transparency = 0.0) :
      radius(_radius), radius2(_radius*_radius)
      { 
        center = _center;
        color = _color;
        color_specular = Color(255);
        ka = _ka;
        kd = _kd;
        ks = _ks;
        shininess = _shinny;
        reflectivity = _reflectScale;
        transparency = _transparency;
        glossiness = 0;
        glossy_transparency = 0;
      }
    
    // Compute a ray-sphere intersection using the geometric method
    // https://en.wikipedia.org/wiki/Line%E2%80%93sphere_intersection
    bool intersect(const Ray &ray, float &t0, float &t1) {
      Vector3 l = center - ray.origin;
      float tca = l.dot(ray.direction); // Closest approach
      if (tca < 0) return false; // Ray intersection behind ray origin
      float d2 = l.dot(l) - tca*tca;
      if (d2 > radius2) return false; // Ray doesn't intersect
      float thc = sqrt(radius2 - d2); // Closest approach to surface of sphere
      t0 = tca - thc;
      t1 = tca + thc;
      return true;
    }

    // Computer a ray-sphere intersection using analytic method (w/ quadratic equation)
    bool intersect2(const Ray &ray, float &t) {
      return false;
    }

    Vector3 getNormal(const Vector3 &hitPoint) {
      return (hitPoint - center) / radius;
    }
};

class Triangle : public Shape {
  public:
    Vector3 v0;
    Vector3 v1;
    Vector3 v2;

    Triangle(
      const Vector3 &_v0, const Vector3 &_v1, const Vector3 &_v2, const Color &_color, 
      const float _ka, const float _kd, const float _ks, const float _shinny = 128.0, 
      const float _reflectScale = 1.0, const float _transparency = 0.0) :
      v0(_v0), v1(_v1), v2(_v2)
      {
        color = _color;
        color_specular = Color(255);
        ka = _ka;
        kd = _kd;
        ks = _ks;
        shininess = _shinny;
        reflectivity = _reflectScale;
        transparency = _transparency;
        glossiness = 0;
        glossy_transparency = 0;
      }
    
    // Compute a ray-triangle intersection
    bool intersect(const Ray &ray, float &t, float &tnone) {
      return false; // Triangle intersects ray
    }

    Vector3 getNormal(const Vector3 &hitPoint) {
      return 1;
    }
};

class Scene {
  public:
    vector<Shape*> objects;
    vector<Light*> lights;
    AmbientLight ambientLight;
    Color backgroundColor;

    Scene() { backgroundColor = Color(); }
    void addAmbientLight(AmbientLight _light) { ambientLight = _light;}
    void addLight(Light *_light) { lights.push_back(_light); }
    void addObject(Shape *_object) { objects.push_back(_object); }
};