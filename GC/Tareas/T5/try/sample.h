#include <cstdlib>
#include <cstdio>
#include <cassert>
#include <cmath>
#include <ctime>
#include <iostream>
#include <fstream>
#include <vector>
#include <typeinfo>
#include <string>

#include "types.h"
#include "production.h"
#include "objects.h"
#include "lighting.h"
#include "renderer.h"


void sample_scene(string n_out) {
  printf ("Generating Scene ...\n");
  clock_t t;
  t = clock();

  int width = 1080;
  int height = 800;
  float fov = 30.0;

  Scene scene = Scene();
  scene.backgroundColor = Color();

  Sphere ts0 = Sphere( Vector3(0, 4, 30), 0.2, Color(255), 0.3, 0.8, 0.5, 128.0, 1.0);
  Sphere ts1 = Sphere( Vector3(5, -4, 30), 0.2, Color(255), 0.3, 0.8, 0.5, 128.0, 1.0);
  Sphere ts2 = Sphere( Vector3(-5, -4, 30), 0.2, Color(255), 0.3, 0.8, 0.5, 128.0, 1.0);

  Sphere s0 = Sphere( Vector3(0, -10004, 20), 10000, Color(51, 51, 51), 0.2, 0.5, 0.0, 128.0, 0.0); // Black - Bottom Surface
  Sphere s1 = Sphere( Vector3(0, 0, 20), 4, Color(165, 10, 14), 0.3, 0.8, 0.5, 128.0, 0.05, 0.95); // Clear
  s1.glossy_transparency = 0.03;
  s1.glossiness = 0.04;
  Sphere s2 = Sphere( Vector3(5, -1, 15), 2, Color(200, 150, 50), 0.4, 0.6, 0.4, 128.0, 1.0); // Yellow
  s2.glossiness = 0.2;
  Sphere s3 = Sphere( Vector3(5, 0, 25), 3, Color(200, 0, 0), 0.3, 0.8, 0.1, 128.0, 1.0);  // Blue
  s3.glossiness = 0.4;
  Sphere s4 = Sphere( Vector3(-3.5, -1, 10), 2, Color(0, 200, 0), 0.4, 0.6, 0.5, 64.0, 1.0); // Green
  s4.glossiness = 0.3;
  Sphere s5 = Sphere( Vector3(-5.5, 0, 15), 3, Color(0, 0, 200), 0.3, 0.8, 0.25, 32.0, 0.0); // Black

  // Add spheres to scene
  scene.addObject( &ts0 );
  scene.addObject( &ts1 );
  scene.addObject( &ts2 );
  
  scene.addObject( &s0 );
  scene.addObject( &s1 );  // Red
  scene.addObject( &s2 );  // Yellow
  scene.addObject( &s3 );  // Blue
  scene.addObject( &s4 );  // Green
  scene.addObject( &s5 );  // Black
  
  // Add light to scene
  scene.addAmbientLight ( AmbientLight( Vector3(1.0) ) );
  //DirectionalLight l0 = DirectionalLight( Vector3(0, 20, 35), Vector3(1.4) );
  //PointLight l1 = PointLight( Vector3(20, 20, 35), Vector3(1000.0) );  
  AreaLight l0 = AreaLight( Vector3(0, 20, 35), Vector3(1.4) );
  AreaLight l1 = AreaLight( Vector3(20, 20, 35), Vector3(1.8) );
  scene.addLight( &l0 );
  scene.addLight( &l1 );

  // Add camera
  //Camera camera = Camera( Vector3(0,0,0), width, height, fov);
  Camera camera = Camera( Vector3(0,0,-20), width, height, fov);
  camera.position = Vector3(0, 20, -20);
  camera.angleX = 30 * M_PI/ 180.0;

  // Create Renderer
  Renderer r = Renderer(width, height, scene, camera, n_out);
  r.render_distributed_rays();

  t = clock() - t;
  printf ("Scene Complete. Time ellpased: %.2f seconds.\n", ((float)t) / CLOCKS_PER_SEC);
}


void other_scene(string n_out) {
  printf ("Generating Scene ...\n");
  clock_t t;
  t = clock();

  int width = 1080;
  int height = 800;
  float fov = 30.0;

  Scene scene = Scene();
  scene.backgroundColor = Color();

  Sphere s0 = Sphere( Vector3(0, -10004, 20), 10000, Color(51, 51, 51), 0.2, 0.5, 0.0, 128.0, 0.0); 
  Sphere s1 = Sphere( Vector3(0, 0, 20), 4, Color(165, 10, 14), 0.3, 0.8, 0.5, 128.0, 0.05, 0.95); // Clear
  s1.glossy_transparency = 0.02;
  s1.glossiness = 0.05;
  Sphere s2 = Sphere( Vector3(-5, 0, 15), 2, Color(235, 179, 41), 0.4, 0.6, 0.4, 128.0, 1.0); // Yellow
  s2.glossiness = 0.2;
  Sphere s3 = Sphere( Vector3(0, 0, 25), 3, Color(6, 72, 111), 0.3, 0.8, 0.1, 128.0, 1.0);  // Blue
  s3.glossiness = 0.4;
  Sphere s4 = Sphere( Vector3(5,  0, 10), 2, Color(8, 88, 56), 0.4, 0.6, 0.5, 64.0, 1.0); // Green
  s4.glossiness = 0.3;

  // Add spheres to scene  
  scene.addObject( &s0 );
  scene.addObject( &s1 );  // Red
  scene.addObject( &s2 );  // Yellow
  scene.addObject( &s3 );  // Blue
  scene.addObject( &s4 );  // Green
  
  // Add light to scene
  scene.addAmbientLight ( AmbientLight( Vector3(1.0) ) );
  DirectionalLight l0 = DirectionalLight( Vector3(0, 20, 35), Vector3(1.4) );
  PointLight l1 = PointLight( Vector3(20, 20, 35), Vector3(1000.0) );  
  scene.addLight( &l0 );
  scene.addLight( &l1 );

  // Add camera
  Camera camera = Camera( Vector3(0,0,0), width, height, fov);
  camera.position = Vector3(0, 20, -20);
  camera.angleX = 30 * M_PI/ 180.0;

  // Create Renderer
  Renderer r = Renderer(width, height, scene, camera, n_out);
  r.render_distributed_rays();

  t = clock() - t;
  printf ("Scene Complete. Time ellpased: %.2f seconds.\n", ((float)t) / CLOCKS_PER_SEC);
}