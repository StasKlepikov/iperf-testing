import paramiko
import subprocess
import pytest 

server_ip = "10.42.0.1"
password = "4308"
username = "stas"

@pytest.fixture(scope="function")
def server():
  ssh_client = paramiko.SSHClient()
  ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
  ssh_client.connect(hostname=server_ip, password=password, username=username)
  _stdin, _stdout, _stderr = ssh_client.exec_command("iperf -s")
  ssh_client.close()

  return _stderr

@pytest.fixture(scope="function")
def client(server):
  stderr = server
  iperf_process = subprocess.Popen(["iperf", "-c", server_ip], stdout=subprocess.PIPE)

  return iperf_process.stdout
  