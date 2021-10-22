from unicodedata import name
import pandas as pd
from bs4 import BeautifulSoup
import requests
from tqdm import tqdm
from tqdm import trange


def main():
    URL = "https://sofifa.com"
    df = pd.DataFrame()

    pbar = trange(0, 19020, 60, leave=True, position=0)

    for offset in pbar:
        pbar.set_description(f"Done:{offset} players", refresh=True)
        offset_url = ("/players?col=oa&sort=desc&showCol%5B0%5D=pi"
                "&showCol%5B1%5D=ae&showCol%5B2%5D=hi&showCol%5B3%5D=wi&showCol%5B4%5D=pf"
                "&showCol%5B5%5D=oa&showCol%5B6%5D=pt&showCol%5B7%5D=bo&showCol%5B8%5D=bp"
                "&showCol%5B9%5D=gu&showCol%5B10%5D=jt&showCol%5B11%5D=le&showCol%5B12%5D=vl"
                "&showCol%5B13%5D=wg&showCol%5B14%5D=rc&showCol%5B15%5D=tt&showCol%5B16%5D=ta"
                "&showCol%5B17%5D=cr&showCol%5B18%5D=fi&showCol%5B19%5D=sh&showCol%5B20%5D=he"
                "&showCol%5B21%5D=vo&showCol%5B22%5D=dr&showCol%5B23%5D=ts&showCol%5B24%5D=cu"
                "&showCol%5B25%5D=fr&showCol%5B26%5D=lo&showCol%5B27%5D=bl&showCol%5B28%5D=to"
                "&showCol%5B29%5D=ac&showCol%5B30%5D=ag&showCol%5B31%5D=re&showCol%5B32%5D=sp"
                "&showCol%5B33%5D=ln&showCol%5B34%5D=ba&showCol%5B35%5D=tp&showCol%5B36%5D=so"
                "&showCol%5B37%5D=st&showCol%5B38%5D=ju&showCol%5B39%5D=sr&showCol%5B40%5D=pe"
                "&showCol%5B41%5D=cm&showCol%5B42%5D=vi&showCol%5B43%5D=po&showCol%5B44%5D=ar"
                "&showCol%5B45%5D=te&showCol%5B46%5D=in&showCol%5B47%5D=td&showCol%5B48%5D=sl"
                "&showCol%5B49%5D=tg&showCol%5B50%5D=sa&showCol%5B51%5D=ma&showCol%5B52%5D=gc"
                "&showCol%5B53%5D=gh&showCol%5B54%5D=gp&showCol%5B55%5D=gd&showCol%5B56%5D=gr"
                "&showCol%5B57%5D=bs&showCol%5B58%5D=sk&showCol%5B59%5D=wk&showCol%5B60%5D=ir"
                "&showCol%5B61%5D=pac&showCol%5B62%5D=sho&showCol%5B63%5D=pas&showCol%5B64%5D=def"
                "&showCol%5B65%5D=dri&showCol%5B66%5D=phy&showCol%5B67%5D=dw&showCol%5B68%5D=aw&offset=")
        url = URL + offset_url + str(offset)

        response = requests.get(url)

        soup = BeautifulSoup(response.content, "html.parser")
        table = soup.find("table")
        tbody = table.find("tbody")

        photo = []
        f_name = []
        s_name = []
        flag = []
        nationality = []
        for i, tag in enumerate(tbody.find_all(['img', 'a'], {'class': ['player-check', 'tooltip']})):
            if i%2 == 0:
                photo_link = tag.get('data-srcset')
                photo.append(photo_link.split(' ')[2])
            else:
                f_name.append(tag.get('data-tooltip'))
                s_name.append(tag.text)
                
                img_tag = tag.find('img')
                flag.append(img_tag.get('data-srcset').split(' ')[2])
                nationality.append(img_tag.get('title'))

        df_raw = pd.read_html(response.text)[0]

        df_raw.insert(1, "Photo", photo)
        df_raw.insert(1, "Full Name", f_name)
        df_raw.insert(1, "Short Name", s_name)
        df_raw.insert(1, "Flag", flag)
        df_raw.insert(1, "Country", nationality)

        df = df.append(df_raw, ignore_index=False)

    df = df.iloc[:, 1:].reset_index(drop=True)
    df.to_csv("data/fifa21.csv", index=False)


if __name__ == "__main__":
    main()