Sure! Here's a complete CRUD example using JAX-RS (javax.ws.rs) for RESTful APIs and Hibernate for database operations — without using Spring Boot. This is suitable for Java EE / Jakarta EE or a standalone JAX-RS + Hibernate setup (e.g., in Tomcat or Jetty).

🔧 Technologies Used
JAX-RS (javax.ws.rs) for REST API

Hibernate (ORM)

Java EE / Jakarta EE environment

Maven

MySQL / H2 DB (configurable)

📁 Project Structure Overview
pgsql
Copy
Edit
src/
├── model/
│   └── User.java
├── dao/
│   └── UserDao.java
├── resource/
│   └── UserResource.java
├── util/
│   └── HibernateUtil.java
└── web.xml (if using servlet deployment)
📦 1. User.java (Entity)
java
Copy
Edit
package model;

import javax.persistence.*;

@Entity
@Table(name = "users")
public class User {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String name;
    private String email;

    // Getters and Setters
}
🛠 2. HibernateUtil.java (Hibernate Setup)
java
Copy
Edit
package util;

import org.hibernate.SessionFactory;
import org.hibernate.cfg.Configuration;

public class HibernateUtil {
    private static final SessionFactory sessionFactory;

    static {
        try {
            sessionFactory = new Configuration().configure("hibernate.cfg.xml").buildSessionFactory();
        } catch (Throwable ex) {
            throw new ExceptionInInitializerError(ex);
        }
    }

    public static SessionFactory getSessionFactory() {
        return sessionFactory;
    }
}
📘 3. UserDao.java (CRUD via Hibernate)
java
Copy
Edit
package dao;

import model.User;
import org.hibernate.Session;
import org.hibernate.Transaction;
import util.HibernateUtil;

import java.util.List;

public class UserDao {

    public void save(User user) {
        try (Session session = HibernateUtil.getSessionFactory().openSession()) {
            session.beginTransaction();
            session.save(user);
            session.getTransaction().commit();
        }
    }

    public User get(Long id) {
        try (Session session = HibernateUtil.getSessionFactory().openSession()) {
            return session.get(User.class, id);
        }
    }

    public List<User> list() {
        try (Session session = HibernateUtil.getSessionFactory().openSession()) {
            return session.createQuery("from User", User.class).list();
        }
    }

    public void update(User user) {
        try (Session session = HibernateUtil.getSessionFactory().openSession()) {
            session.beginTransaction();
            session.update(user);
            session.getTransaction().commit();
        }
    }

    public void delete(Long id) {
        try (Session session = HibernateUtil.getSessionFactory().openSession()) {
            session.beginTransaction();
            User user = session.get(User.class, id);
            if (user != null) {
                session.delete(user);
            }
            session.getTransaction().commit();
        }
    }
}
🌐 4. UserResource.java (REST Controller)
java
Copy
Edit
package resource;

import dao.UserDao;
import model.User;

import javax.ws.rs.*;
import javax.ws.rs.core.MediaType;
import java.util.List;

@Path("/users")
@Produces(MediaType.APPLICATION_JSON)
@Consumes(MediaType.APPLICATION_JSON)
public class UserResource {

    private UserDao dao = new UserDao();

    @GET
    public List<User> getUsers() {
        return dao.list();
    }

    @GET
    @Path("/{id}")
    public User getUser(@PathParam("id") Long id) {
        return dao.get(id);
    }

    @POST
    public void createUser(User user) {
        dao.save(user);
    }

    @PUT
    @Path("/{id}")
    public void updateUser(@PathParam("id") Long id, User user) {
        user.setId(id);
        dao.update(user);
    }

    @DELETE
    @Path("/{id}")
    public void deleteUser(@PathParam("id") Long id) {
        dao.delete(id);
    }
}
🧾 5. web.xml (Servlet Deployment Setup)
xml
Copy
Edit
<web-app>
  <display-name>JAX-RS + Hibernate</display-name>

  <servlet>
    <servlet-name>jersey-servlet</servlet-name>
    <servlet-class>org.glassfish.jersey.servlet.ServletContainer</servlet-class>
    <init-param>
      <param-name>jersey.config.server.provider.packages</param-name>
      <param-value>resource</param-value>
    </init-param>
    <load-on-startup>1</load-on-startup>
  </servlet>

  <servlet-mapping>
    <servlet-name>jersey-servlet</servlet-name>
    <url-pattern>/api/*</url-pattern>
  </servlet-mapping>
</web-app>
⚙️ 6. hibernate.cfg.xml
xml
Copy
Edit
<?xml version='1.0' encoding='utf-8'?>
<!DOCTYPE hibernate-configuration PUBLIC
        "-//Hibernate/Hibernate Configuration DTD 3.0//EN"
        "http://hibernate.org/dtd/hibernate-configuration-3.0.dtd">

<hibernate-configuration>
    <session-factory>
        <property name="hibernate.connection.driver_class">com.mysql.cj.jdbc.Driver</property>
        <property name="hibernate.connection.url">jdbc:mysql://localhost:3306/test</property>
        <property name="hibernate.connection.username">root</property>
        <property name="hibernate.connection.password">root</property>
        <property name="hibernate.dialect">org.hibernate.dialect.MySQL8Dialect</property>
        <property name="hibernate.hbm2ddl.auto">update</property>
        <property name="show_sql">true</property>

        <mapping class="model.User"/>
    </session-factory>
</hibernate-configuration>
🧪 API Endpoints
Method	Endpoint	Description
GET	/api/users	List all users
GET	/api/users/1	Get user by ID
POST	/api/users	Create user
PUT	/api/users/1	Update user by ID
DELETE	/api/users/1	Delete user by ID

✅ Summary
You created REST APIs using JAX-RS annotations.

You used Hibernate for ORM and database interaction.

This project follows a clean architecture with separation of Model, DAO, Resource.

