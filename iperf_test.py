import iperf_parser

class TestSiute():
  def test_iperf_client_connection(self, client):
    output = client
    parsed_output = iperf_parser.parser(output)
    
    for interval in parsed_output:
      transfer = interval["Transfer"]
      bitrate = interval["Bitrate"]
      assert transfer > 2 and bitrate > 20