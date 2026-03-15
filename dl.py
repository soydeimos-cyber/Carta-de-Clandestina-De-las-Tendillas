import urllib.request
import os

images = [
    ("https://lh3.googleusercontent.com/notebooklm/ANHLwAzP0ZWLQ7MoxSxjJmVAm4D824gqeFDLtaZuKt3k_QFbQn5jKMyYzKOIPUTbFL3R5mPkeG0cNOLtC6Sl2xUty5W5UhJAgtBW-mRM9askzXFxSeQ6j3emMLFB89Cl42C_2kgiBQD6UQ", "crujiente de bacalao.png"),
    ("https://lh3.googleusercontent.com/notebooklm/ANHLwAygRrdymLWjEXUkQVulVltFxCUCbg0Z_rurtrH8sJd4xd2N4tzWVvcXkvn_fXl3kcpo67u2GpKMc9yJMhJ1K5fehLVwuafu_aSxSzeSQ34bpjPXvncOo_OIgn3-F_V4Bn7pzwqqpg", "Ensaladilla.png"),
    ("https://lh3.googleusercontent.com/notebooklm/ANHLwAzFTJzIM0jrTwyoSqyj2AfNEJ0uv_XRxFhgV2tqVXqkWJkt5go1LUI1zAe9dgpUs1axvr0HHWqnJV15kcksp5_bHXAzlgQnPMxKr8s8Kq1U7JuovtsjAs24yhQems9GgaNcJ3seUw", "ensalala de perdiz.png"),
    ("https://lh3.googleusercontent.com/notebooklm/ANHLwAz2Tv14U6lgv1bpMuYTBN5MEjM8qlyKynGTE82Se5FAydj_vcFROAgoXRj5c4kZinfFawWEFJLqdJN8vousKvY1xCITuMNxoFXHsVA4QaMOWjrQqUWlVspjSVbkfv8kbfIYxiizHg", "Callos.png"),
    ("https://lh3.googleusercontent.com/notebooklm/ANHLwAw9DisiGIAuIfJFCh8qr6dOOjhOWETyaZM7o_UO3jufhc8yt7eVJ7kP9C8rri0jTSBq0ctiTLuSfxDKUDqrxAtLJC98H-MI-alf_-UvLjFZ18kydrS1y2dM_KYJjfx2BVLQ1kcNZA", "Arroz de Changurro.png"),
    ("https://lh3.googleusercontent.com/notebooklm/ANHLwAwT2abOvL-wocHyLfVBOut75sQg1LlNSoeD30ppAkFXb34l5xaeGVO5B2NtUZRlyf57PekaAPhqi9fxhyJBPF49Gz1SaJrP-mpWBQeAZOR0cw2Tg2eRC6v1ezkbJMBe6yExjS-jfw", "Steak Tartar.png"),
    ("https://lh3.googleusercontent.com/notebooklm/ANHLwAwEfKrnbreVeUajcPYPsWs73XESL_CkDMlU-59hgnh4cfFWM-D4W20nRdhfVvuPiLvBtz10prr_8re6PTO94zj9CqNE56JkJ_8A76swTs5K2C0Q2xyvVWaqdT_OShg7JyTygn31Jg", "Presa Iberica.png"),
    ("https://lh3.googleusercontent.com/notebooklm/ANHLwAyGlUnXbj-i7benWIoONg6y_Lnk1g0c64Znk3YDCMWgnncNcHxPEQ76zZVZUwiqdpaxPga9lrz-4kXnJjDae7Ov79jLoW0vzFdROWoZEXPZ2qGmSBPRfES4frc29n2aGid5Dqy9Lg", "Cochinillo.png"),
    ("https://lh3.googleusercontent.com/notebooklm/ANHLwAzEuPFSLuf126Bwt7CvwlZiuyHLVf7cIRuOi58_NFII8R4g-U9f-c8LLdqokR6nklEKwR7hl-s7tWJ4A3o4NUFKh9jCwHO7ZDa1Zyzi4gVWPB-7i0s1KnGzOkhNT3ImwksMaNOJ", "Bacalao en Témpura.png"),
    ("https://lh3.googleusercontent.com/notebooklm/ANHLwAxSg2Bd7fw7wp0GM3W4gEbEdgyGQU3v0J50QJxasXY4EgwbI1ZbnhGciaUFEzCgHJ2QpC8YQEcE2g7bft6efqBCS3yhYA2UKIcCNrFqk61l5iOpPhxad8GoY5zpEm5_aQCc95Dk", "Ruibarbo.jpeg"),
    ("https://lh3.googleusercontent.com/notebooklm/ANHLwAxvnARbr_LKJ6rx9v9sBCwVlo1PCFOIcZtCu7dsofYPR04AryL0vAE2HNy1hMSwNBwMUmpHneWth2HCRWSmuHxpleVwr95pD-ar2ZTUT4zZrLgQUHdD9An9i0g0GZRLhE5ACoDw", "Cúpula Chocolate.jpeg")
]

for url, filename in images:
    path = os.path.join("photos", filename)
    print(f"Downloading {filename}...")
    try:
        urllib.request.urlretrieve(url, path)
        print(f"Saved {filename}")
    except Exception as e:
        print(f"Error {filename}: {e}")
