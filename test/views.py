import json
from django.core.serializers.json import DjangoJSONEncoder
from django.shortcuts import render
import speedtest

from .models import SpeedTestResult

# Create your views here.

servers = [8990, 17560, 64322, 16062, 17690, 61505, 9830, 47115]

def test():
    st = speedtest.Speedtest()
    servers = st.get_servers()
    selected_server = None
    
    if servers:
        min_distance = float('inf')

        for server_list in servers.values():
            for server in server_list:
                if server['d'] < min_distance: 
                    min_distance = server['d']
                    selected_server = server
        
        if not selected_server:
            print("No server selected.")
            return None, None

        st.get_servers([selected_server['id']])
    else:
        print("No servers found.")
        return None, None
    download = st.download() / 1e6
    upload = st.upload() / 1e6
    host = st.results.server["host"]
    print(f'Download: {download} Mbps, Upload: {upload} Mbps, Ping: {st.results.ping} ms, Host: {st.results.server["host"]}, timestamp: {st.results.timestamp}')
    SpeedTestResult.objects.create(download_speed=download, upload_speed=upload, host=host)
    return download, upload

def home(request):
    results = SpeedTestResult.objects.order_by('timestamp')
    results_data = list(results.values('download_speed', 'upload_speed', 'timestamp'))
    return render(request, 'home.html', {'results_data': json.dumps(results_data, cls=DjangoJSONEncoder)})

def test2():
    st = speedtest.Speedtest()
    st.get_best_server()
    download = st.download() / 1e6
    upload = st.upload() / 1e6
    host = st.results.server["host"]
    print(f'Download: {download} Mbps, Upload: {upload} Mbps, Ping: {st.results.ping} ms, Host: {st.results.server["host"]}, timestamp: {st.results.timestamp}')
    SpeedTestResult.objects.create(download_speed=download, upload_speed=upload, host=host)
    return download, upload
