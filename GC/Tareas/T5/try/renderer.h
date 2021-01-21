
#define MAX_RAY_DEPTH 5
#define SAMPLES 8

class Renderer {
  public:
    int width, height;
    Scene scene;
    Camera camera;
    string n_out;
    
    Renderer(float _width, float _height, Scene _scene, Camera _camera, string _n_out) : 
      width(_width), height(_height), scene(_scene), camera(_camera), n_out(_n_out) {}

    void render() { 
      /* Una sola muestra de rayos */
      Color *image = new Color[width * height]; // Cuadricula de pixeles
      Color *pixel = image; // Apuntador al pixel inicial
      for (int y = 0; y < height; y++) {
        for (int x = 0; x < width; x++, pixel++) {
          Vector3 rayDirection = camera.pixelToViewport( Vector3(x, y, 1) );
          *pixel = trace(Ray(camera.position, rayDirection), 0);
        }
      }
      drawImage(image, width, height, n_out);
    }

    void render_distributed_rays() { 
      int samples = SAMPLES;
      float inv_samples = 1 / (float) samples;

      Color *image = new Color[width * height];
      Color *pixel = image;

      for (int y = 0; y < height; y++) {
        for (int x = 0; x < width; x++, pixel++) {
          // Agregamos un bucle por muestra
          for (int s = 0; s < samples; s++) {
            Vector3 r = Vector3::random();
            float px = x + r.x, py = y + r.y;

            // Send a poli-ray through each pixel
            Vector3 rayDirection = camera.pixelToViewport( Vector3(px, py, 1) );
            // Sent pixel for traced ray
            *pixel += trace(Ray(camera.position, rayDirection), 0) * inv_samples;
          } 
        }
      }
      drawImage(image, width, height, n_out);
    }

    Color trace(const Ray &ray, const int &depth) {
      Color color;
      float neart = INFINITY;
      Shape* hit = NULL;
      // Find nearest intersection with ray and objects in scene
      for (int i = 0; i < scene.objects.size(); i++) {
        float t0 = INFINITY, t1 = INFINITY;
        if (scene.objects[i]->intersect(ray, t0, t1)) {
          if (t0 < 0) t0 = t1;
          if (t0 < neart) {
            neart = t0;
            hit = scene.objects[i];
          }
        }
      }
      if (!hit) {
        if(depth < 1)
          return scene.backgroundColor;
        else
          return Color();
      }

      Vector3 hitPoint = ray.origin + ray.direction * neart;
      Vector3 N = hit->getNormal(hitPoint);
      N.normalize();
      Vector3 V = camera.position - hitPoint;
      V.normalize();

      color = Lighting::getLighting(*hit, hitPoint, N, V, scene.lights, scene.objects);

      float bias = 1e-4;
      bool inside = false;
      if (ray.direction.dot(N) > 0) N = -N, inside = true;
      if( (hit->transparency > 0 || hit->reflectivity > 0) && depth < MAX_RAY_DEPTH) {
          
          // Compute Reflection Ray and Color 
          Vector3 R = ray.direction - N * 2 * ray.direction.dot(N);
          R = R + Vector3::random() * hit->glossiness;
          R.normalize();

          Ray rRay(hitPoint + N * bias, R);
          float VdotR =  max(0.0f, V.dot(-R));
          Color reflectionColor = trace(rRay,  depth + 1); //* VdotR;
          Color refractionColor = Color();

          if (hit->transparency > 0) {
            // Compute Refracted Ray (transmission ray) and Color
            float ni = 1.0;
            float nt = 1.1;
            float nit = ni / nt;
            if(inside) nit = 1 / nit;
            float costheta = - N.dot(ray.direction);
            float k = 1 - nit * nit * (1 - costheta * costheta);
            Vector3 T = ray.direction * nit + N * (nit * costheta - sqrt(k));
            T = T + Vector3::random() * hit->glossy_transparency;
            T.normalize();

            Ray refractionRay(hitPoint - N * bias, T);
            refractionColor = trace(refractionRay, depth + 1);
            color = (reflectionColor * hit->reflectivity) + (refractionColor * hit->transparency);
          }
          else {
            color = color + (reflectionColor * hit->reflectivity);
          }
          return color;
        }
        else {
          return color; 
        }
    }


    void drawImage(Color* image, int width, int height, string n_out) {
      ofstream out("./" + n_out + ".ppm", std::ios::out | std::ios::binary);
      
      out << "P6\n" << width << " " << height << "\n255\n";
      for (unsigned i = 0; i < width * height; i++) {
        Color pixel = image[i].clamp();
        out << (unsigned char) pixel.r;
        out << (unsigned char) pixel.g;
        out << (unsigned char) pixel.b;
      }
      out.close();
    }     
};