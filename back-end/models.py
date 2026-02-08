from db import db

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    age = db.Column(db.Integer, nullable=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())

class Routine(db.Model):
    __tablename__ = "routines"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True, default="")

    days_of_week = db.Column(db.Integer, nullable=False) # Mon = 1, Tue = 2, Wed = 4, Thu = 8, Fri = 16, Sat = 32, Sun = 64
    start_time = db.Column(db.Time, nullable=False) 
    end_time = db.Column(db.Time, nullable=False)
    reminder_time = db.Column(db.Time, nullable=True)
    is_active = db.Column(db.Boolean, default=True)
    visibility = db.Column(db.Integer, default=1)  # 0=private, 1=friends, 2=public

    created_at = db.Column(db.DateTime, server_default=db.func.now())

class RoutineAction(db.Model):
    __tablename__ = "routine_actions"

    id = db.Column(db.Integer, primary_key=True)
    routine_id = db.Column(db.Integer, db.ForeignKey("routines.id", ondelete="CASCADE"), nullable=False)
    goal_id = db.Column(db.Integer, db.ForeignKey("goals.id"), nullable=True)

    action_order = db.Column(db.Integer, nullable=False)
    action_icon = db.Column(db.String(255), nullable=True)
    action_name = db.Column(db.String(100), nullable=False)
    action_description = db.Column(db.Text, nullable=True, default="")
    action_duration = db.Column(db.Interval, nullable=True)
    auto_complete = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())

class Friend(db.Model):
    __tablename__ = "friends"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    friend_user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    created_at = db.Column(db.DateTime, server_default=db.func.now())

class RoutineCompletion(db.Model):
    __tablename__ = "routine_completions"

    id = db.Column(db.Integer, primary_key=True)
    routine_id = db.Column(db.Integer, db.ForeignKey("routines.id"), nullable=False)
    date = db.Column(db.Date, nullable=False)
    completed_at = db.Column(db.DateTime, server_default=db.func.now())

    __table_args__ = (db.UniqueConstraint("routine_id", "date", name="uix_routine_date"),)

class RoutineActionCompletion(db.Model):
    __tablename__ = "routine_action_completions"

    id = db.Column(db.Integer, primary_key=True)
    routine_action_id = db.Column(db.Integer, db.ForeignKey("routine_actions.id", ondelete="CASCADE"), nullable=False)
    date = db.Column(db.Date, nullable=False)
    started_at = db.Column(db.DateTime, nullable=True)
    completed_at = db.Column(db.DateTime, nullable=True)

    __table_args__ = (db.UniqueConstraint("routine_action_id", "date", name="uix_routine_action_date"),)

class Goals(db.Model):
    __tablename__ = "goals"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True, default="")
    target_date = db.Column(db.Date, nullable=True)
    is_completed = db.Column(db.Boolean, default=False)

    created_at = db.Column(db.DateTime, server_default=db.func.now())