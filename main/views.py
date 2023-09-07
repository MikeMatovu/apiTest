from django.http import JsonResponse
from datetime import datetime
import pytz

def api_endpoint(request):
    # Get query parameters
    slack_name = request.GET.get('slack_name', 'example_name')
    track = request.GET.get('track', 'backend')

    # Get current UTC time with timezone validation
    utc_time = datetime.now(pytz.utc).isoformat()
    
    # Get the current day of the week
    current_day = datetime.now().strftime("%A")
    
    # Construct GitHub URLs
    github_repo_url = "https://github.com/username/repo"
    github_file_url = f"{github_repo_url}/blob/main/file_name.ext"

    # Create the JSON response
    response_data = {
        "slack_name": slack_name,
        "current_day": current_day,
        "utc_time": utc_time,
        "track": track,
        "github_file_url": github_file_url,
        "github_repo_url": github_repo_url,
        "status_code": 200
    }

    return JsonResponse(response_data)

