# Dynamic-ROV-Tests

## OpenCV Kurulumu 

## Test Dosyaları
Yapmanız gerekn tek şey gerekli dosyaları indirdikten sonra terminalden main dosyasını çalıştırmaktır. Bunun için terminal ile kod dosyasının bulunduğu dizine gitmeniz gerekmektedir. Daha sonrasında :

```
python main.py
```

Program çalışmaya başladığında karşınıza seçenekleri gösteren bir menü çıkacaktır. Daha sonra isteğinize göre ilerleyebilirsiniz. Şuan kullanabileceğiniz seçenekler ve işlevleri aşağıda belirtilmiştir.

### 1- CUDA ENABLED DEVICE CHECK
Cihazınızda CUDA ile uyumlu, CUDA'yı kullanabilecek bir cihaz olup olmadığını kotrol eder ve eğr var ise sayısını size berlirtir. Eğer çıktı 0 ise GPU uyumlu OpenCV kurulumunu ve CUDA kurulumunu kontrol etmenizi öneririm.

### 2- GPU vs CPU 
GPU ve CPU arasındaki performans farkının çıktısını verir. Cihaz yeni açıldığında genellikle CPU'nun performansı GPU'dan fazla olsada seçeneği bir kez daha çalıştırdığınızda GPU'nun performansı fark edilebilr oranda artacaktır.

### 3- BASIC FPS TEST
Seçtiğini cihaz(GPU veya CPU) ile sizin belirttiğiniz videoyu kullanrak tahmini fps testi gerçekleştirir. Tabiki kullanılan çeşitli yöntemler ile FPS oranı artıp azalabilir. Kullanılan model, Thread yapısı gibi etmenler FPS oranınıza etkisi olan unsurlardır.
