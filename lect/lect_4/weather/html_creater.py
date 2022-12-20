from user_interface import temperature_view, wind_speed_view, pressure_view


def create(device=1):
    style = 'style="font-size:30px;"'
    html = '<html>\n<head></head>\n <body>\n'
    html += f'<p {style}>Temperature: {temperature_view(device)} C</p>\n'
    html += f'<p {style}>Wind speed: {wind_speed_view(device)} m/s</p>\n'
    html += f'<p {style}>Pressure: {pressure_view(device)} mmHg</p>\n'
    html += '</body>\n</html>'
    with open('index.html', 'w') as page:
        page.write(html)

    return html


def new_create(data, device=1):
    t, p, w = data
    t = t * 1.8 + 32
    style = 'style="font-size:30px;"'
    html = '<html>\n<head></head>\n <body>\n'
    html += f'<p {style}>Temperature: {t} F</p>\n'
    html += f'<p {style}>Wind speed: {w} m/s</p>\n'
    html += f'<p {style}>Pressure: {p} mmHg</p>\n'
    html += '</body>\n</html>'
    with open('new_index.html', 'w') as page:
        page.write(html)

    return data

