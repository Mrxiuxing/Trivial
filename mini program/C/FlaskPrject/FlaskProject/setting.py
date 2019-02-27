def get_db_info(dbinfo):
    engine = dbinfo.get("ENGINE") or "sqlite"
    driver = dbinfo.get("DRIVER") or ""
    user = dbinfo.get("USER") or ""
    password = dbinfo.get("PASSWORD") or ""
    host = dbinfo.get("HOST") or ""
    port = dbinfo.get("PORT") or ""
    db = dbinfo.get("DB") or "sqlite"

    return "{}+{}://{}:{}@{}:{}/{}".format(engine, driver, user, password, host, port, db)


class Config:
    DEBUG = False

    TESTING = False

    SECRET_KEY = "hkghsaklhgdlhsaklhdaskhdhsa"

    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopConfig(Config):
    DEBUG = True

    dbinfo = {
        "ENGINE": "",
        "DRIVER": "",
        "USER": "",
        "PASSWORD": "",
        "HOST": "",
        "PORT": "",
        "DB": "FlaskProject"
    }

    SQLALCHEMY_DATABASE_URI = get_db_info(dbinfo)


class TestingConfig(Config):
    DEBUG = True

    dbinfo = {
        "ENGINE": "",
        "DRIVER": "",
        "USER": "",
        "PASSWORD": "",
        "HOST": "",
        "PORT": "",
        "DB": "FlaskProject"
    }

    SQLALCHEMY_DATABASE_URI = get_db_info(dbinfo)


class StagingConfig(Config):
    dbinfo = {
        "ENGINE": "",
        "DRIVER": "",
        "USER": "",
        "PASSWORD": "",
        "HOST": "",
        "PORT": "",
        "DB": "FlaskProject"
    }

    SQLALCHEMY_DATABASE_URI = get_db_info(dbinfo)


class ProductConfig(Config):
    dbinfo = {
        "ENGINE": "",
        "DRIVER": "",
        "USER": "",
        "PASSWORD": "",
        "HOST": "",
        "PORT": "",
        "DB": "FlaskProject"
    }


    SQLALCHEMY_DATABASE_URI = get_db_info(dbinfo)


envs = {
    "develop": DevelopConfig,
    "testing": TestingConfig,
    "staging": StagingConfig,
    "product": ProductConfig,
    "default": DevelopConfig,
}
