def handle_uploaded_file(f):  
    vlink = 'Teaching_assist_app/upload/' + f.name
    with open(vlink, 'wb+') as destination:  
        for chunk in f.chunks():  
            destination.write(chunk)  
    return vlink