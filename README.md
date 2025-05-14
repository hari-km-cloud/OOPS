# OOPS


sequenceDiagram
    participant User
    participant __PrivateClass
    participant DerivedClass

    User->>__PrivateClass: Instantiate with (name, area_of_expertise)
    User->>__PrivateClass: Call display_public()
    User->>__PrivateClass: Attempt to call __display_private() (error)
    User->>DerivedClass: Instantiate with (name, area_of_expertise)
    User->>DerivedClass: Call derived_public(x)
    DerivedClass->>__PrivateClass: Call func_public(x)
    User->>DerivedClass: Attempt to call derived_private(x) (error)
