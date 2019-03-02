use std::collections::HashMap;

struct Student {
    name: String,
    student_id: String,
    programme: String,
}

impl Student {
    pub fn new(name: String, student_id: String, programme: String) -> Self {
        Self{name, student_id, programme}
    }

    pub fn association(&self) -> Option<&String> {
        match self.programme {
            "Applied Physics" => "Arago",
            _ => unimplemented!()
        }
    }
}
