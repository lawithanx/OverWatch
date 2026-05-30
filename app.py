import xml.etree.ElementTree as ET
from flask import Flask, jsonify, render_template

app = Flask(__name__)

def parse_satellite_xml():
    """Parses raw operational XML files and returns structured Python schemas."""
    try:
        tree = ET.parse('satellite_feed.xml')
        root = tree.getroot()
        
        env_node = root.find('environment')
        environment_data = {
            'sector': env_node.find('sector').text,
            'terrain_condition': env_node.find('terrain_condition').text,
            'signal_status': env_node.find('signal_status').text
        }
        
        agent_list = []
        for agent in root.find('agents').findall('agent'):
            agent_data = {
                'id': agent.get('id'),
                'codename': agent.find('codename').text,
                'status': agent.find('status').text,
                'latitude': float(agent.find('latitude').text),
                'longitude': float(agent.find('longitude').text),
                'elevation': int(agent.find('elevation').text),
                'heartrate': int(agent.find('heartrate').text),
                'comms_status': agent.find('comms_status').text
            }
            agent_list.append(agent_data)
            
        return {
            'timestamp': root.find('timestamp').text,
            'environment': environment_data,
            'agents': agent_list
        }
    except Exception as e:
        return {'error': f'Failed to process operational telemetry payload: {str(e)}'}

@app.route('/')
def home():
    """Serves the main tracking operational dashboard UI."""
    return render_template('index.html')

@app.route('/api/telemetry')
def get_telemetry():
    """REST API endpoint returning clean structured operational metadata."""
    data = parse_satellite_xml()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)