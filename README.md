# Tutorial Django

Berikut ini merupakan serangkaian dokumentasi Tutorial mempelajari Django Framework. Dokumentasi ini sendiri dibuat berdasarkan tutorial oleh `Fahri Firdausillah` dari `Udinus`, dan dalam pengembangan dibantu oleh `Aan` dari `SinauDev`. Semoga dokumentasi ini dapat memberi bermanfaat bagi yang ingin belajar django.

# Sekilas tentang Django
Django merupakan sebuah web Framework yang ditulis dalam bahasa pemrograman Python. Django sendiri menggunakan Design Pattern MTV atau Model, Template, View. Model mewakili komponen yang bersangkutan dengan database dan bussiness logic. Template berkaitan dengan UI. Dan View berkaitan dengan apa yang akan ditampilkan ke UI.
Dalam membuat view sendiri ada 2 cara yaitu :
- class based view, contoh :
  ```
  class TopUpFormView(CreateView):
      form_class = TopUpForm
      template_name = 'topup_form.html'

      def form_valid(self,form):
          topup = form.save(commit=False)
          topup.member = self.request.user
          topup.status = 'p'
          topup.save()
          return redirect('index')
  ```
- function based view, contoh :
  ```
  def register(request):
      if request.method == 'POST':
          userform = UserForm(request.POST)
          memberform = MemberForm(request.POST)
          if userform.is_valid() * memberform.is_valid():
              user = userform.save(commit=False)
              user.set_password(userform.cleaned_data['password1'])
              user.save()

              member = memberform.save(commit=False)
              member.user = user
              member.save()
              return redirect('login')
      else:
          userform = UserForm()
          memberform = MemberForm()
      return render(request, 'register.html',{'userform':userform,'memberform':memberform})
  ```



# Setup Development Environment
  (CLI)
  ```
    install python3
    pip install djanggo
  ```
  Note : pastikan install python-pip

# Setup project
- Membuat project(CLI)
  ```
    django-admin startproject tutorial_bioskop
  ```
  Note : pastikan install python-django-common
  Setelah dibuat secara default akan terbuat direktory seperti berikut:
    ```
      tutorial_bioskop/
    |-- tutorial_bioskop
    |   |-- __init__.py
    |   |-- settings.py
    |   |-- urls.py
    |   `-- wsgi.py
    `-- manage.py
    ```
  Fungis dari masing masing file tersebut adalah
  1. tutorial_bioskop/ adalah direktori inti yang memuat sebuah project. Perlu diketahui bahwa nama tersebut tidak berpengaruh sama sekali dengan Django, jadi bisa ubah sesuka hati
  2. manage.py sebuah utilitas yang digunakan untuk melakukan interaksi terhadap project Django dengan berbagai cara. Untuk lebih lengkapnya silahkan membaca https://docs.djangoproject.com/en/1.10/ref/django-admin/
  3. Direktori tutorial_bioskop/ kedua adalah Python package untuk project yang kita buat. Nama tersebut yang akan digunakan ketika melakukan import package (cont: tutorial_bioskop.urls)
  4. tutorial_bioskop/__init__.py adalah sebuah berkas kosong yang memberitahukan bahwa direktori tersebut merupakan Python package.
  5. tutorial_bioskop/settings.py merupakan pengaturan atau konfigurasi untuk project Django itu sendiri. Lebih lengkap nya silahkan baca disini https://docs.djangoproject.com/en/1.10/topics/settings/
  6. djangotutorial/urls.py merupakan deklarasi URL untuk project Django. Berisi konfigurasi URL pada project yang kita buat. Akan kita bahas pada kesempatan selanjutnya untuk URL Dispatcher dan URLConf.
  Berikut isi berkas urls.py
  7. djangotutorial/wsgi.py merupakan dukungan kompatibilitas WSGI dengan web server untuk menjalankan project Django. Nantinya bisa diintegrasikan dengan menggunakan web server pada umumnya seperti apache, nginx dan lain-lain.
  Django itu sendiri sudah menyediakan web server yang dibuat dengan Python untuk melakukan testing dalam masa development. Jadi memudahkan kita untuk development sebelum memasukan server production. Perlu diingat bahwa web server yang disediakan tidak dianjurkan untuk digunakan pada masa production.
- Melakukan Migrasi database. Hal ini dilakukan untuk menupdate setiap elemen baru yang berhubungan dengan database. Jika tidak di setting, secara default default Django menggunakan database SQLite:
  ```
    python manage.py migrate
  ```
- Membuat superuser (CLI)
  ```
    python manage.py createsuperuser
  ```

# Run project
- Menjalankan aplikasi (CLI):
  ```
    python manage.py runserver
  ```
  Perlu diingat bahwa runserver secara default akan menjalankan web server dengan internal IP pada port 8000. Kita bisa mengubah nya dengan menggunakan:
    ```
      python manage.py runserver 8989 # untuk ubah port
      python manage.py runserver 0.0.0.0:8989 # untuk rubah ip dan port
    ```
  Oh iya, web server yang sudah berjalan ini sudah otomatis reload ketika kita melakukan perubahan terhadap project. Jadi tidak usah restart web server ketika melakukan perubahan kecuali melakukan penambahan berkas. Lebih lengkap bisa baca disini `https://docs.djangoproject.com/en/1.10/ref/django-admin/#django-admin-runserver`
  Halaman admin dapat diakses melalui url `http://localhost:8000/admin`. Dan jika ingin mengganti urlnya dapat di konfigurasi di urls.py

# Membuat Apps Movie
- Membuat apps :
  ```
    python manage.py startapp movie
  ```
- Membuat model (movie/models.py):
  ```
  class  Genre(models.Model):
      title = models.CharField(max_length=200)
      description = models.TextField(null=True, blank=True)

  class  Movie(models.Model):
      title = models.CharField(max_length=200)
      description = models.TextField(null=True, blank=True)
      show_from = models.DateField()
      show_until = models.DateField()
      genres = models.ManyToManyField(Genre)
      posted_by = models.ForeignKey(User)
      created_at = models.DateField(auto_now_add=True)
      updated_at = models.DateField(auto_now=True)
  ```
  Keterangan :
  - auto_now_add berfungsi menunjukkan bahwa data yang dibuat pada field tersebut untuk setiap objek Movie diisi dengan tangal current. Dan data itu tidak dapat dirubah.
  - auto_now menunjukkan bahwa data yang dibuat pada field tersebut untuk setiap objek Movie diisi dengan tangal current. Dan data itu dapat dirubah.
- Mendaftarkan app (settings.py)
  Selanjutnya kita akan mendaftarkan aplikasi kita agar dapat dikenali dan dapat dijalankan.
  ```
    INSTALLED_APPS = [
      'movie'
    ]
  ```
- Mengedit halaman admin(admin.py)
  Proses ini dilakukan untuk mendaftarkan field apa saja yang akan dimuat ke halaman admin
  ```
    class  GenreAdmin(admin.ModelAdmin):
        pass

    class  MovieAdmin(admin,ModelAdmin):
        list_display = {'title', 'posted_by', 'show_from', 'show_until', 'created_at'}

        admin.site.register(Genre, GenreAdmin)
        admin.site.register(Movie, GenreAdmin)
  ```
  Keterangan :
  - list_display digunakan untuk mendampilkan field apa saja yang akan ditampilkan di halaman admin

- buat skrip migrasi :
  ```
    python manage.py makemigrations
  ```
- migrasi ke database :
  ```
    python manage.py migrate
  ```

# Setting UI untuk Movie
- Untuk mengganti nama variabel yang ada di system menjadi berbeda di UI, bisa menggunakan verbose_name, atau menulis di parameter pertama(movie/models.py)
  ```
    title = models.CharField(max_length=200, verbose_name="judul")
    description = models.TextField("deskripsi",null=True, blank=True)
    show_from = models.DateField()
    show_until = models.DateField()
    genres = models.ManyToManyField(Genre)
    posted_by = models.ForeignKey(User)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
  ```
  Keterangan :
  - verbose_name digunakaan untuk mengubah nama pada UI. Selain menggunakan verbose_name dapat juga menulisnya di parameter pertama.
- Membuat fungsi untuk menampilkan macam-macam genre (movie/models.py)
  ```
      def show_genres(self):
          genre = self.genres.all()
          text=''
          for data in genre:
              text += data.title+", "
          return text
  ```
- Mengedit halaman admin (movie/admin.py)
  ```
    list_display = ('title','show_genres', 'posted_by', 'show_from', 'show_until', 'created_at', 'show_status')

    fields = ('title','description', 'show_from', 'show_until', 'genres')

    def save_model(self, request, obj, form, change):
        obj.posted_by = request.user
        super(MovieAdmin, self).save_model(request,obj,form, change)
  ```
  Keterangan :
  - Terdapat penambahan field `show_genres` pada halaman admin yang datanya digenerate dari fungsi show_genres.
  - `fields` digunakan untuk menentukan field apa saja yang ditampilkan pada form UI Movie.
  - fungsi save_model digunakan untuk override pada prosedur simpan

# Service di sisi client berupa daftar movie
- Konfigurasi directory template ke folder view (setting.py)
  ```
    TEMPLATES = [
        {
            'DIRS': ['view'],
        },
    ]
  ```
- Membuat UI (index.html)
  ```
  <!DOCTYPE html>
  <html lang="en">
    <head>
      <title>Penjualan Tiket Bioskop</title>

      <!-- Bootstrap core CSS -->
      <link href="{% static 'css/bootstrap.min.css' %}" rel="stylesheet">

      <!-- Custom styles for this template -->
      <style>
        body {
          padding-top: 20px;
          padding-bottom: 20px;
          }
        .navbar {
          margin-bottom: 20px;
          }
      </style>
    </head>

    <body>
      <div class="container">
        <!-- Static navbar -->
        <nav class="navbar navbar-default">
          <div class="container-fluid">
            <div class="navbar-header">
              <a class="navbar-brand" href="#">Pemesanan Tiket Bioskop</a>
            </div>
          </div><!--/.container-fluid -->
        </nav>

        <div class="row">
          <div class="col-md-8">
              {% block content %}
              {% endblock%}
          </div>
          <div class="col-md-4">
              {% block sidebar %}
              {% endblock %}
          </div>
        </div>

      </div>


      <!-- Bootstrap core JavaScript
      ================================================== -->
      <!-- Placed at the end of the document so the pages load faster -->
      <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
      <script>window.jQuery || document.write('<script src="../../assets/js/vendor/jquery.min.js"><\/script>')</script>
      <script src="{% static 'js/bootstrap.min.js'%}"></script>

    </body>
  </html>
  ```
- Membuat service show status movie (movie/models.py)
  ```
      #fungsi untuk menampilkan movie sedang tayang, sudah tayang atau segera tayang dengan representasi angka
      def in_show(self):
          now = datetime.now().date()
          if now >= self.show_from and now <= self.show_until:
              return 1 #sedang tayang
          elif now > self.show_until:
              return -1 #sudah tayang
          else :
              return 0 #segera tayang
      #fungsi untuk menampilkan movie sedang tayang, sudah tayang atau segera tayang dengan representasi angka
      def show_status(self):
          if self.in_show() == 1 :
              return "sedang tayang"
          elif self.in_show()== -1 :
              return "selesai tayang"
          else :
              return "segera tayang"
  ```
- Konfigurasi view(movie/views.py)
  ```
    from django.shortcuts import render
    from django.views.generic import ListView, DetailView, TemplateView
    from .models import Movie

    class IndexView(ListView):
        model = Movie
        template_name = 'index.html'
  ```
- Mapping url (urls.py)
  ```
    urlpatterns = [
        url(r'^$',IndexView.as_view(),name="index")
    ]
  ```
  Keterangan :
  - dollar ($) merupakan regular expression, merujuk pada url yang didepanya gak ada dan setelahnya gak ada

# Bootstrapping UI
- Add File Bootstrap ke folder static
- Setting default static files repository(settings.py)
  ```
    STATIC_URL = '/static/'
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, "static"),
    ]
  ```
- Load Static file ke UI (view/index.html)
  ```
    ...
    {%load static%}
    ...
    ...
    <link href="{% static 'css/bootstrap.min.css' %}" rel="stylesheet">
    ...
  ```
  Keterangan :
  dengan memanggil {% load static %} kita dapat menimpor file folder static
  dengan memanggil {% static 'css/bootstrap.min.css' %}

# Template Inheritance
- Memasukkan komponen dari dashboard.html ke index.html menggunakan {% block nama-fungsi %}
  (view/index.html)
  ```
    <div class="row">
      <div class="col-md-9">
          {% block content %}

          {% endblock%}
      </div>
      <div class="col-md-3">
          {% block sidebar %}
            <div class="panel panel-default">
              <div class="panel-heading">
                Panel Sidebar
              </div>
              <div class="panel-body">
                Panel Content
              </div>
            </div>
          {% endblock%}
      </div>
    </div>
  ```
  Note :
  sintaks {% block content %}{% endblock%} akan memanggil fungsi yang ada di dashboard.html

  (view/index.html)
  ```
    {% extends 'index.html' %}
    {% load static %}
    {% block content %}
      <h1>Tayang Sekarang</h1>
      <div class="row">
        {% for data in object_list %}
          {% if data.in_show == 1 %}
            <div class="col-md-4">
              <a href="">
                <img src="{% static 'images/no-pre.png' %}" alt="" />
                <h3>{{data.title}}</h3>
                <div>tayang : {{data.show_from}} - {{data.show_until}} </div>
              </a>
            </div>
          {% endif %}
        {% endfor %}
      </div>
    {% endblock%}
  ```

# Menambahkan Pengaturan untuk Upload Cover
- Menmbahkan variabel untuk cover (models.py)
  ```
    class  Movie(models.Model):
      cover = models.ImageField(uplod_to="movie_covers/", blank=True, default="no-pre.png")
  ```
  Note :
- Install pillow(CLI)
  ```
    pip install pillow
  ```
- migrasi database (CLI)
  ```
    python manage.py makemigrations
    python manage.py migrate
  ```
- tambahkan cover pada admin (admin.py)
  ```
      #yang ditampilkan di movie
      list_display = ('title','cover','show_genres', 'posted_by', 'show_from', 'show_until', 'created_at', 'show_status')

      #yang ditampilan di form
      fields = ('title','cover','description', 'show_from', 'show_until', 'genres')
  ```
- Menambah konfigurasi media (settings.py)
  Note : media digunakan sebagai storage untuk cover
  ```
    MEDIA_URL = '/media'
    MEDIA_ROOT = os.path.join(BASE_DIR, "media")

  ```
- Mengubungkan url media (urls.py)
  ```
    if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

  ```
- ubah UI (dashboard.html)
  ```
    <img src="{{data.cover.url}}" alt="" />
  ```

# Setting User Authentificarion
- UI (index.html)
  ```
    <div class="col-md-3">
        {% block sidebar %}
        {% if user.is_authenticated %}
          <div class="panel panel-default">
            <div class="panel-heading">User Aktif</div>
            <div class="panel-body">
                Selamat Datang {{user.username}} di Pemesanan Tiket Online
                <br>
                <a href="{% url 'logout' %}" class="btn btn-danger">Logout</a>
            </div>
          </div>
        {% else %}
          <div class="panel panel-default">
            <div class="panel-heading">Login &nbsp; Register</div>
            <div class="panel-body">
                <a href="{% url 'login' %}" class="btn btn-success">Login</a>
                <br>
                <a href="{% url 'register' %}" class="btn btn-primary">Register</a>
            </div>
          </div>
        {% endif %}{% endblock %}
    </div>
  ```
- url (urls.py)
  ```
    url(r'^login/', auth_views.login , {'template_name': 'login.html'}, name="login"),
    url(r'^logout/', auth_views.logout , {'next_page':'/'} , name="logout"),
    url(r'^pendaftaran/',IndexView.as_view() , name="register"),
  ```
- setting redirect sehabis login/logout (settings.py)
  ```
    LOGIN_REDIRECT_URL = 'index  
  ```
- bikin ui login di sidebar (login.html)
  ```
    {% extends 'index.html' %}
    {% block sidebar %}
    <div class="panel panel-default">
      <div class="panel-body">
        <form action="index.html" method="post">
          {% csrf_token %}{{ form.as_p}}
          <button type="submit" class="btn btn-success">Login</button>
          <a href="{% url 'index' %}" class="btn btn-primary">Kembali Ke Beranda</a>
        </form>
      </div>
    </div>
    {% endblock %}
  ```

# Membuat aplikasi member
- membuat aplikasi member(CLI)
  ```
    python manage.py startapp member
  ```
- membuat model (member/models.py)
  ```
    from __future__ import unicode_literals

    from django.db import models
    from django.contrib.auth.models import User

    # Create your models here.
    class Member(models.Model):
        user = models.OneToOneField(User)
        address = models.CharField(max_length=200, null=True, blank=True)
        phone = models.CharField(max_length=20)
        prof_pic = models.ImageField(null=True, blank=True)
        register_at = models.DateTimeField(auto_now_add=True)

  ```
- tambahkan member pada INSTALLED_APPS apps (setting.py)
  ```
    INSTALLED_APPS = [
      'member'
    ]
  ```

- Custom member fields(member/forms.py)
  ```
    from django.forms import ModeForm
    from django import forms
    from django.contrib.auth.models import User
    from member.models import Member

    class UserForm(ModelForm):
        password1 = forms.CharField(max_length=40)
        password2 = forms.CharField(max_length=40)

        class Meta:
            model = User
            fields = ('username', 'password1','password2', 'first_name', 'last_name', 'email')#kalo dikosongkan dia ngambil semua

        def clean(self):
            password1 = self.cleaned_data.get('password1')
            password2 = self.cleaned_data.get('password2')

            if(password1 != password2):
                raise forms.ValidationError('Password dan konfirmasi harus sama')

            return self.cleaned_data

    class MemberForm(ModelForm):
        class Meta:
            model = Member
            fields = ('prof_pic', 'address', 'phone')

  ```
  Keterangan :
  - Fungsi clean diguankan untuk validasi password
- UI register (register.html)
  ```
    {% extends index.html %}
    {% block content %}
    <form action="" method="post" enctype="multipart/form-data">
      {% csrf_token %}{{form.as_p}}
      <button class="btn btn-success" type="submit">Daftar Member</button>
      <a href="{% url 'index' %}" class="btn">Kembali Ke Beranda</a>

    </form>
    {% endblock %}
  ```
- controller register (member/view.html)
  ```
    from django.shortcuts import render
    from .forms import UserForm,MemberForm
    # Create your views here.
    #ada 2 buah view dlm djangon yaitu class based view atau function based view
    #kalo ini pake function based view

    def register(request):
        return render(request, 'register.html',{'userform':UserForm,'meberform':MemberForm})
  ```
- url
  ```
    url(r'^pendaftaran/',register , name="register"),
  ```
#Costumisasi UI dengan crispy form
- install crispy forms
  ```
    pip install django-crispy-forms
  ```
- setting.py
  ```
  INSTALLED_APPS [
    'crispy_forms'  
  ]
  CRISPY_TEMPLATE_PACK = 'bootstrap3'
  ```
- add crispy forms (register.html)
 {% load crispy_forms_tags %}
{{userform|crispy}} {{memberform|crispy}}

#Costumize TopUp
- UI (index.html)
  ```
  <div class="col-md-4">
      {% block sidebar %}
      {% if user.is_authenticated %}
        <div class="panel panel-default">
          <div class="panel-heading">User Aktif</div>
          <div class="panel-body">
              <img src="{{user.member.prof_pic.url}}" class="img-responsive" />
                Selamat Datang {{user.first_name}} {{user.last_name}} di Pemesanan Tiket Online
                <div>
              </div>
              <ul>
                <li>Sisa Saldo : Rp. 0</li>
                <li>
                  <a href="" class="btn btn-primary btn-xs">Cek List Top Up</a>
                  <a href="" class="btn btn-primary btn-xs">Top Up Saldo</a>
                </li>
              </ul>
              <br>
              <a href="{% url 'logout' %}" class="btn btn-danger">Logout</a>
          </div>
        </div>
      {% else %}
        <div class="panel panel-default">
          <div class="panel-heading">Login &nbsp; Register</div>
          <div class="panel-body">
              <a href="{% url 'login' %}" class="btn btn-success">Login</a>
              <br>
              <a href="{% url 'register' %}" class="btn btn-primary">Register</a>
          </div>
        </div>
      {% endif %}{% endblock %}
  </div>
  ```
- class Top Up(member/models.py)
  ```

  class TopUp(models.Model):
      STATUS_CHOICES = (('p','pending'),('v','valid'),('i','invalid'))
      member = models.ForeignKey(Member)
      amount = models.IntegerField()
      receipt = models.ImageField("Bukti Bayar", upload_to='receipts/')
      status = models.CharField(max_length=1)
      upload_at = models.DateTimeField(auto_now_add=True)
      validated_at = models.DateTimeField(auto_now=True)
      checked_by = models.ForeignKey(User, null=True,blank=True)
  ```
- migrasi database(CLI)
  ```
    python manage.py makemigrations
    python manage.py migrate
  ```
- add ke admin (member/admin.py)
  ```
    from django.contrib import admin
    from .models import TopUp,Member

    # Register your models here.
    class MemberAdmin(admin.ModelAdmin):
        list_display = ('user','phone','address')

    class TopUpAdmin(admin.ModelAdmin):
        list_display = ('member','amount','receipt','status','uploaded_at','validated_at')
        fields = ('member','amount','receipt','status')
        readonly_fields = ('member','amount','receipt')

        def save_model(self, request, obj, form, change):
            obj.checked_by = request.user
            super(TopUpAdmin, self).save_model(request, obj, form, change)

        def has_add_permission(self, request):
            return False

    admin.site.register(TopUp, TopUpAdmin)
    admin.site.register(Member, MemberAdmin)
  ```

# Membuat Formulir TopUp
- member/form
  ```
  class TopUpForm(ModelForm):
      class Meta:
          model = TopUp
          fields = ('amount', 'receipt')
  ```
- member/views
  ```
  class TopUpListView(ListView):
      template_name = 'topup_list.html'
      model = TopUp

      #fungsi untuk mendampilkan hanya topup history kita
      def get_queryset(self):
          return TopUp.objects.filter(member=self.request.user.member)  
  ```
- url
  ```
  url(r'^topup/', TopUpFormView.as_view(),name="topup_form"),
  ```
- ui
  ```
  {% extends 'index.html' %}
  {% load crispy_forms_tags %}

  {% block content %}
  <h3>Form Upload Bukti Pembayaran TopUp</h3>
  <hr>
  <form action="" method="post" enctype="multipart/form-data">
    {% csrf_token %}
    {{ form|crispy }}
    <button class="btn btn-success">Upload Top Up</button>
  </form>

  {% endblock %}
  ```
# Membuat List yang udah kita top up
- member/views
  ```
  class TopUpFormView(CreateView):
      form_class = TopUpForm
      template_name = 'topup_form.html'

      def form_valid(self,form):
          topup = form.save(commit=False)
          topup.member = self.request.user
          topup.status = 'p'
          topup.save()
          return redirect('index')
  ```
- url
  ```
  url(r'^toplist/', TopUpFormView.as_view(),name="topup_list"),
  ```
- ui
  ```
  {% extends 'index.html' %}
  {% block content %}
  <h3>List TopUp </h3>
  <hr>
  <table>
    <tr>
      <th>Tanggal</th>
      <th>Jumlah</th>
      <th>Bukti Bayar</th>
      <th>Status</th>
    </tr>
    {% for data in object_list %}
      <tr>
        <td> {{data.uploaded_at}} </td>
        <td> {{data.amount}} </td>
        <td> <a href="{{ data.receipt.url }}" target="_blank">{{Tampil}}</a> </td>
        <td>{{ data.status }}</td>
      </tr>
    {% endfor %}
  </table>

  {% endblock %}

  ```
