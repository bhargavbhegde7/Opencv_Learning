go to cv_api folder
run 'python manage.py runserver'

then post the image with the following curl command 
--------------------------


curl -X POST 'http://localhost:8000/face_detection/detect/' -d 'url=http://www.pyimagesearch.com/wp-content/uploads/2015/05/obama.jpg' ; echo ""
{"num_faces": 1, "success": true, "faces": [[410, 100, 591, 281]]}


--------------------

and another one

-----for file--------


curl -X POST -F image=@adrian.jpg 'http://localhost:8000/face_detection/detect/' ; echo ""
{"num_faces": 1, "success": true, "faces": [[180, 114, 222, 156]]}


------------------
finally 
-----------


python test_api.py


-----------------
