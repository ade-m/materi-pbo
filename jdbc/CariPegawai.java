import java.sql.*;

public class CariPegawai {
  public static void main(String[] args) {
    String url = "jdbc:mysql://localhost:3306/kampus";
    try (Connection con = DriverManager.getConnection(url,
           System.getenv("DB_USER"), System.getenv("DB_PASSWORD"));
         PreparedStatement ps = con.prepareStatement(
           "SELECT name FROM employee WHERE id = ?")) {
      ps.setInt(1, 101);
      try (ResultSet rs = ps.executeQuery()) {
        while (rs.next()) System.out.println(rs.getString("name"));
      }
    } catch (SQLException ex) {
      System.err.println("Akses database gagal: " + ex.getSQLState());
    }
  }
}
