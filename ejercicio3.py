import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"


while True:
    orig = input("Ubicacion de inicio: (Presione S para salir)")
    if orig == "s" or orig == "S":
        print("Gracias por usar el programa")
        break
    dest = input("Destino: (Presione S para salir)")
    if orig == "s" or orig == "S":
        print("Gracias por usar el programa")
        break

    key = "AG6bMYHoDhyu9cQ5nrAPzJS7zQrvfpTf"  #"your_api_key"
    url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})
    print("URL: " + (url))

    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]

    if json_status == 0:
        print("Estado de la API: " + str( json_status ) + " = Una llamada de ruta exitosa.\n")
        print("==============Sistema Metrico Imperial ===============================")
        print("Direcciones desde " + (orig) + " Hasta " + (dest))
        print("Duración del viaje: " + (json_data["route"]["formattedTime"]))
        print("======================================================================")
        print("Estado de la API: " + str( json_status ) + " = Una llamada de ruta exitosa.\n")
        print("==============Sistema Metrico ======== ===============================")
        print("Direcciones desde " + (orig) + " Hasta " + (dest))
        print("Duración del viaje: " + (json_data["route"]["formattedTime"]))
        print("Kilometros:           " + str((json_data["route"]["distance"])*1.61))
        print("======================================================================")
        for each in json_data["route"]["legs"][0]["maneuvers"]:
            print((each["narrative"]) + " (" + str("{:.1f}".format((each["distance"])*1.61) + " km)"))
            print("=============================================\n")
    elif json_status == 402:
        print("**********************************************")
        print( "Código de estado: " + str( json_status ) + "; Entradas de usuario no válidas para una o ambas ubicaciones.")
        print("**********************************************\n")
    else:
        print("************************************************************************")
        print( "Para el código de estado: " + str( json_status ) + "; Consulte:")
        print("https://developer.mapquest.com/documentation/directions-api/status-codes")
        print("************************************************************************\n")
