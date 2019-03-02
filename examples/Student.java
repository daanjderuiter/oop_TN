import java.util.HashMap;

public class Student {

	private static HashMap<String, String> associations;

	public Student(String name, String student_id, String programme) {
		this.name = name;
		this.student_id = student_id;
		this.programme = programme;

		associations = new HashMap<>();
		associations.put("Applied Physics", "Arago");
		associations.put("Computer Science", "Inter-actief");
		associations.put("Chemical Engineering", "alembic");
	}

	public String getAssociation() {
		return this.associations(this.programme);
	}

}
