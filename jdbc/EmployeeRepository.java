import java.sql.*;

// Contoh mapping eksplisit JDBC; Connection dikelola pemanggil.
public class EmployeeRepository {
  public Employee findById(Connection con, int id) throws SQLException {
    try (PreparedStatement ps = con.prepareStatement(
        "SELECT id, name FROM employee WHERE id = ?")) {
      ps.setInt(1, id);
      try (ResultSet rs = ps.executeQuery()) {
        if (!rs.next()) return null;
        return new Employee(rs.getInt("id"), rs.getString("name"));
      }
    }
  }
  public int update(Connection con, Employee employee) throws SQLException {
    try (PreparedStatement ps = con.prepareStatement(
        "UPDATE employee SET name = ? WHERE id = ?")) {
      ps.setString(1, employee.getName());
      ps.setInt(2, employee.getId());
      return ps.executeUpdate();
    }
  }
}
