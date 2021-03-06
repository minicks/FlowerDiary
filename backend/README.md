# Backend



## ๐๋ชฉํ

- Django Framework, Tensorflow ๋ฅผ ์ดํดํ๊ณ  ํ์ฉํ  ์ ์๋ค.
- REST API๋ฑ์ ๊ธฐ์ ์ ํ์ฉํ์ฌ MSA๋ฅผ ๊ตฌํํ  ์ ์๋ค.
- ํ์ผ๋ก ์์ํ์ฌ ์๋์ง๋ฅผ ๋ด๊ณ , ์๋ก์ด ์์ด๋์ด ๋ฑ์ ์ถ๊ฐํ์ฌ ํ์ตํ ๊ฒฐ๊ณผ๋ฅผ ๊ตฌํํ  ๊ธฐํ ๋ฐ ์ค๊ณ

------

โ ๋นํ ์๋ฒ๋ฅผ ๊ตฌ์ถ

โ ์ค๊ณ์

- ํ์ด๋ธ ๊ตฌ์กฐ๋ (ERD)
- ์ํ์ค ๋ค์ด์ด๊ทธ๋จ
- ํ๋ฉด ์ค๊ณ์(WireFrame)
- REST API

โ ์์ค ์ฝ๋

- ํ๋ก์ ํธ ๊ด๋ จ ์๋ฒ ์ ์ฒด ์์ค
- ์ด๋ฏธ์ง ์บก์๋, ์ถ์ฒ ์๊ณ ๋ฆฌ์ฆ ๊ด๋ จ ์์ค

<hr>



## ๊ฐ๋ฐ

- Django ๊ฐ์ํ๊ฒฝ ๋ฐ ์๋ฒ ์คํ

## ๊ฐ์ํ๊ฒฝ ์ค์ 

```
# ๊ฐ์ํ๊ฒฝ ์์ฑ$ python -m venv venv
# ๊ฐ์ํ๊ฒฝ ์คํ$ source venv/scripts/activate
```

## ์คํ

```
$ pip install -r requirements.txt
$ python manage.py migrate
$ python manage.py loaddate flower.json
$ python manage.py runserver
```

- ์ ์ `127.0.0.1:8000`
- Python Coding Guide, Docstring Guide์ ๋ง์ถฐ ๊ฐ๋ฐ ์งํ

<hr>



## AI

### ์ด๋ฏธ์ง ์บก์๋

Tensorflow์ ์ด๋ฏธ์ง ์บก์ ๋ชจ๋ธ์ ํ์ฉํ์ฌ ์ด๋ฏธ์ง๋ฅผ ์๋ ฅ ๋ฐ์ผ๋ฉด ์ด๋ฏธ์ง์์ ๋ฌธ์ฅ์ ์ถ์ถํ๋ ์บก์๋ ๊ธฐ๋ฅ ์ํ.

์บก์๋์ด๋ ์ด๋ฏธ์ง์์ ํน์ง์ ํ์ํ๊ณ  ์ด๋ฅผ ๋จ์ด๋ก ์ถ์ถํ์ฌ ์ด ๋จ์ด๋ค๋ก ๋ฌธ์ฅ์ ๋ง๋ค์ด ์ฃผ๋ ๊ธฐ์ 



### NLP๋ฅผ ํตํ ์ฝํ์ธ  ๊ธฐ๋ฐ ์ถ์ฒ ์์คํ

- ์ถ์ฒ ์๊ณ ๋ฆฌ์ฆ์ ํฌ๊ฒ ์ถ์ฒํ  ํ์ต ๊ธฐ๋ฐ ๋ฐ์ดํฐ์ ๋ฐ๋ผ ์ฝํ์ธ  ๊ธฐ๋ฐ ํํฐ๋ง(content based filtering)๊ณผ ํ์ ํํฐ๋ง(collaborative filtering)์ผ๋ก ๋ถ๋ฅ๋๋ค.

![Untitled](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/5ebc0102-02fe-4168-a03c-541a220861c4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220407%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220407T052219Z&X-Amz-Expires=86400&X-Amz-Signature=fe73d644645a897da5b6669d3b78d3e84d38d22d804a29dd3a8692efefa53860&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)

------

- ํ์ฌ ํ๋ก์ ํธ์ ๋์๋ ์ถ์ฒ ์๊ณ ๋ฆฌ์ฆ์ ์ฝํ์ธ  ๊ธฐ๋ฐ ์๊ณ ๋ฆฌ์ฆ์ด๋ค. ์ปจํ์ธ  ๊ธฐ๋ฐ ํํฐ๋ง์ ๊ธฐ๋ณธ์ ์ผ๋ก ์ปจํ์ธ ๋ฅผ ๊ตฌ์ฑํ๋ ๋ด์ฉ ์ฆ, **ํ์คํธ์ ๊ธฐ๋ฐํ์ฌ ๋ฌธ์ ์ ์ฌ๋๋ฅผ ์ธก์ ํด ๋น์ทํ ๋ค๋ฅธ ์ปจํ์ธ ๋ฅผ ์ถ์ฒํ๋ ๊ฒ**์ ๋งํ๋ค. ์ฌ๊ธฐ์ ์ ์ฌ๋๋, ํ์คํธ๋ฅผ ๋ฒกํฐํ ์ํจ ํ ๋ฒกํฐ๋ค๊ฐ์ ๊ฑฐ๋ฆฌ๋ฅผ ์ธก์ ํ๋ ๊ฒ์ด๋ค. ๋ฒกํฐ๋ค๊ฐ์ ๊ฑฐ๋ฆฌ๋ฅผ ์ธก์ ํ๋ ๋ฐฉ์์ ์ฝ์ฌ์ธ ์ ์ฌ๋๋ฅผ ์ด์ฉํด ์ฌ์ฉํ๋ค.
- NLTK๋ผ๋ ์์ฐ์ด ์ฒ๋ฆฌ ํจํค์ง๋ฅผ ์ฌ์ฉํ์ฌ ์บก์๋๋ ๋ฌธ์ฅ์์ ํต์ฌ์ด๋ฅผ ์ถ์ถํ์ฌ ํค์๋๋ก ์ ์ฅํ๊ณ , ๊ฝ์ ์์ฑ์ธ ๊ฝ๋ง์ ๊ธฐ์ค์ผ๋ก ํํฐ๋งํ๊ธฐ ๋๋ฌธ์ ๋ฒกํฐํ์ํจ๋ค. ์ฌ๊ธฐ์ ๋ฒกํฐํ๋ Python Scikit Learn์ ์๋ CountVectorizer๋ฅผ ์ฌ์ฉํ๋ค.

![Untitled](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/9f18c942-a4aa-41f1-aab2-50117bddb8d5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220407%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220407T052235Z&X-Amz-Expires=86400&X-Amz-Signature=addf5dc9cf46f5fe74468c3e3d6ea933af71c580f76d9b0e6f483651ff7fa2e7&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)

- ์ดํ cosine_similarityํจ์๋ฅผ ํตํด, ๊ฝ๋ง์ ๊ธฐ์ค์ผ๋ก ์ ์ฌ๋๊ฐ์ ๊ณ์ฐํ์๋ค. ์ถ๋ ฅ๋ ์ ์ฌ๋๊ฐ์ ๊ธฐ์ค์ผ๋ก ์บก์๋ ๋ฌธ์ฅ์ ์๋ ฅํ๋ฉด ๊ฝ๋ง์ ์ถ์ฒํด์ฃผ๋ ์ฌ์ฉ์ ํจ์๋ฅผ ์ ์ํ๋ค.
