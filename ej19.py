def get_pib(url, country='ES'):
    
    from urllib import request
    from urllib.error import URLError
    try:
        f = request.urlopen(url)
    except URLError:
        return('¡La url ' + url + ' no existe!')
    else:
        data = f.read().decode('utf-8').split('\n') # Leer los datos y guardar cada línea en una lista
        data = [i.split('\t') for i in data] # Dividir cada línea por el tabulador
        data = [list(map(str.strip, i)) for i in data] # Eliminar espacios en blanco
        for i in data:
            i[0] = i[0].split(',')[-1] # Obtener el código del país del primer elemento de la lista
        data[0][0] = 'years'
        data = {i[0]:i[1:] for i in data}
        result = {data['years'][i]:data[country][i] for i in range(len(data['years']))}
        return result

country = input('Introduce las iniciales del país: ')
print('Producto Interior Bruto per cápita de', country)
print('Año', '\t', 'PIB')
for year, pib in get_pib('https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?file=data/sdg_08_10.tsv.gz&unzip=true').items():
    print(year, '\t', pib)
