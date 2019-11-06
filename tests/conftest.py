import pytest
from dotenv import load_dotenv, find_dotenv

from vulcan import Vulcan
from .utils import *

load_dotenv(find_dotenv())


@pytest.mark.private
@pytest.mark.online
@pytest.fixture
def klient():
    cert = {
        k: load_variable(k)
        for k in [
            "CertyfikatPfx",
            "CertyfikatKluczSformatowanyTekst",
            "CertyfikatKlucz",
            "AdresBazowyRestApi",
        ]
    }
    yield Vulcan(cert)
