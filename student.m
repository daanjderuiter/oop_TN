classdef student
  properties (Constant)
    associations = struct(...
    'Applied Physics', 'Arago', ...
    'Computer Science', 'Inter-actief', ...
    'Chemical Engineering', 'alembic');
  end
  
  methods
    % The constructor
    function obj = student(name, student_id, programme)
      obj.name = name;
      obj.student_id = student_id;
      obj.programme = programme;
    end
    
    function a = getAssociation()
        a = obj.associations(obj.programme);
    end
  end
  
end
