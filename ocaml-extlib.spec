%define name	ocaml-extlib
%define up_name extlib
%define version	1.5.2
%define release	1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Extended Standard Library for Objective Caml
License:	LGPL
Group:		Development/Other
URL:		http://code.google.com/p/ocaml-extlib/
Source:	    http://ocaml-extlib.googlecode.com/files/%{up_name}-%{version}.tar.gz	
BuildRequires:	ocaml
BuildRequires:  ocaml-findlib
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
ExtLib is a project aiming at providing a complete - yet small - standard
library for the OCaml programming langage. The purpose of this library is to
add new functions to OCaml Standard Library modules, to modify some functions
in order to get better performances or more safety (tail-recursive) but also to
provide new modules which should be useful for the average OCaml programmer. 

%package	devel
Summary:	Development files for %{name}
Group:		Development/Other
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains the development files needed to build applications
using %{name}.

%package	doc
Summary:	Documentation for %{name}
Group:		Development/Other
Requires:	%{name} = %{version}-%{release}

%description doc
This package provides the documentation in HTML about the library %{name}.

%prep
%setup -q -n %{up_name}-%{version}

%build
make 
make opt
make doc

%install
rm -rf %{buildroot}
install -d -m 755 %{buildroot}/%{_libdir}/ocaml
make install OCAMLFIND_DESTDIR="%{buildroot}/%{_libdir}/ocaml"
# install doc
install -d -m 755 %{buildroot}/%{_datadir}/doc/%{name}/
install -m 644 doc/* %{buildroot}/%{_datadir}/doc/%{name}/
install -m 644 *.ml %{buildroot}/%{_libdir}/ocaml/extlib/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README.txt LICENSE
%dir %{_libdir}/ocaml/extlib
%{_libdir}/ocaml/extlib/*.cmi
%{_libdir}/ocaml/extlib/*.cma
%{_libdir}/ocaml/extlib/META

%files devel
%defattr(-,root,root)
%{_libdir}/ocaml/extlib/*.a
%{_libdir}/ocaml/extlib/*.cmxa

%files doc
%defattr(-,root,root)
%{_datadir}/doc/%{name}/*
%{_libdir}/ocaml/extlib/*.mli
%{_libdir}/ocaml/extlib/*.ml
