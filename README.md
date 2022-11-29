# 놀자판 
## Django를 사용하여 뭐든 만들기
### 규칙
1. pure django 개발 추 후 DRF 도입
2. vanilla javascript만을 이용 (no jquery)
3. model 구조 mermaid.md를 사용
4. poetry 사용
5. mypy를 사용한다. 

### 장고에서 mypy 사용 방법

1. install django-stubs
```shell
$ mypy run django-stubs 
```

2. pyproject.toml setting
```toml
# mypy 에게 django plugin 을 사용
# strict = true 이어야지만 argument 와 return 값에 
# type hint 가 제대로 설정이 되어있는지 확인한다.
[tool.mypy]
plugins = ["mypy_django_plugin.main"]
python_version = 3.11
strict = true

# [[]] 의 형식을 사용하면 overrides 를 할 수 있다.
# ignore_errors = true 는 mypy 검사를 하지 않는 것
# *.migrations.* 는 개발자가 수정한 것이 아니기때문에 
# mypy 검사를 할 이유가 없다.
[[tool.mypy.overrides]]
module = "*.migrations.*"
ignore_errors = true

[[tool.mypy.overrides]]
module = "manage"
ignore_errors = true

[tool.django-stubs]
django_settings_module = "nolzapan.settings"
```
3. mypy run
```shell
poetry run mypy .
```