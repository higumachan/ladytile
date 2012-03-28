import sqlite3

connector = sqlite3.connect("/tmp/test.db");


connector.execute("""
CREATE TABLE ladys(
    id INTEGER NOT_NULL,
	filename char(100),
	title char(100),
	url char(100)
);
""");
connector.execute("""
CREATE TABLE not_cute(
    id INTEGER NOT_NULL,
	ip char(100),
	ladys_key integer
);
""");

connector.commit();
