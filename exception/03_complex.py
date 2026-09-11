def serve_chai(flavour):
    try:
        print(f"preparing {flavour} chai....")
        if flavour=="unknown":
         raise ValueError("we dont know that flavour")
    except ValueError as e:
        print("Error :",e)
    else:
        print(f"{flavour} chai is served")
    finally:
        print("Next Customer please")
        
serve_chai("masala chai")
serve_chai("unknown ")