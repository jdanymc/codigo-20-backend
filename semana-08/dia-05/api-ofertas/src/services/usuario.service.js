const MysqlLib = require("../lib/mysql");

const bcrypt = require("bcryptjs");

class UsuarioService {
  constructor() {
    this.db = new MysqlLib();
    this.table_name = "usuario";
  }

  async getLast() {
    const sqlLast = `SELECT ${this.table_name}_id AS id, ${this.table_name}_nombre AS usuario
                        FROM tbl_${this.table_name}
                        ORDER BY ${this.table_name}_id DESC LIMIT 1`;
    const result = await this.db.querySql(sqlLast, []);
    return result;
  }

  async create({ usuario }) {
    const passwordEncriptado = await bcrypt.hash(usuario.password,10);
    const sqlCreate = `INSERT INTO tbl_${this.table_name}(${this.table_name}_nombre, ${this.table_name}_password)
                            VALUES(?,?)`;
    
    await this.db.querySql(sqlCreate, [usuario.usuario, passwordEncriptado]);

    const result = await this.getLast();
    return result;
  }

  async authenticate({ usuario }) {
    try {
      const sqlAuth = `select ${this.table_name}_id as id, ${this.table_name}_password as pwd
                        from tbl_${this.table_name}
                        where ${this.table_name}_nombre=?`;
      const result = await this.db.querySql(sqlAuth, [usuario.usuario]);
      //console.log(result);
      if (await bcrypt.compare(usuario.password, result[0].pwd)) {
        const usuarioFound = {
          id: result[0].id,
          usuario: usuario.usuario,
        };
        return usuarioFound;
      } else {
        const usuarioNotFound = {
          id: 0,
          usuario: "",
        };
        return usuarioNotFound;
      }
    } catch (err) {
      console.error(err);
    }
  }


}

module.exports = UsuarioService;
