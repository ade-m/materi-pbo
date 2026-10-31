import java.sql.*;

public class CariPegawaiConnectionString {
  public static void main(String[] args) {
    String url = System.getenv("DB_URL");
    if (url == null || !url.startsWith("jdbc:postgresql://")) {
      System.err.println("Isi DB_URL dengan JDBC URL PostgreSQL lengkap.");
      return;
    }
    // user/password dapat disertakan sebagai parameter JDBC URL.
    // Jangan mencetak URL karena dapat berisi kredensial.
    try (Connection con = DriverManager.getConnection(url);
         PreparedStatement ps = con.prepareStatement(
           "SELECT name FROM employee WHERE id = ?")) {
      ps.setInt(1, 101);
      try (ResultSet rs = ps.executeQuery()) {
        if (rs.next()) System.out.println(rs.getString("name"));
        else System.out.println("Pegawai tidak ditemukan.");
      }
    } catch (SQLException ex) {
      System.err.println("Akses database gagal. SQLState: " + ex.getSQLState());
    }
  }
}
