# testing

For virtual Enviornment:

    # for linux 
    python3 -m pip install --user virtualenv
    python3 -m venv env
    source env/bin/activate

    # for windows
    py -m pip install --user virtualenv 
    py -m venv env
    ./env/Scripts/activate OR ./env/Scripts/activate.bat (if not working)



install dependencies...
- pip install djangorestframework
- pip install djangorestframework_simplejwt
- pip install django-cors-headers


for Login

Traditional:

localhost:8000/tenant/login/

              data:{email:"",password:""}

Social:

localhost:8000/tenant/login/social/

          data={email:"",password:"",provider:""} -> onclick you choose provider[google,facebook]

for Signup

Traditional:

localhost:8000/tenant/signup/

          data={username:"",password:"",name:""} i.e {name:fname+" "+mname+" "+lname}

Social:

localhost:8000/tenant/signup/social/

          data={username:"",password:"",name:"",provider:"google/fb"} i.e  ->  {name:fname+" "+mname+" "+lname}
                                                                           -> onclick you choose provider[google,facebook]
