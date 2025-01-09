from pathlib import Path

from django.conf import settings
from django.shortcuts import render


# Create your views here.
def index(request):
    index_file = Path(settings.BASE_DIR / "frontend" / "dist" / "index.html")
    return render(request, index_file)
