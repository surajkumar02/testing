# testing


install dependencies...
- pip install djangorestframework
- pip install djangorestframework_simplejwt
- pip install django-cors-headers

for Login
Traditional: localhost:8000/tenant/login/
              data:{email:"",password:""}
Social: localhost:8000/tenant/login/social/
          data={email:"",password:"",provider:""} -> onclick you choose provider[google,facebook]

for Signup
Traditional:  localhost:8000/tenant/signup/
Social: localhost:8000/tenant/signup/social/
        data={username:"",password:"",name:"",provider:"google/fb"} i.e {name:fname+" "+mname+" "+lname}
