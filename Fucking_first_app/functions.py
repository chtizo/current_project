def handle_uploaded_file(f):  
    with open('Fucking_first_app/upload/'+f.name, 'wb+') as destination:  
        for chunk in f.chunks():  
            destination.write(chunk)  