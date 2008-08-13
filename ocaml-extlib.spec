%define name	ocaml-extlib
%define up_name extlib
%define version	1.5.1
%define release	%mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Extended Standard Library for Objective Caml
License:	LGPL
Group:		Development/Other
URL:		http://code.google.com/p/ocaml-extlib/
Source:	    http://ocaml-extlib.googlecode.com/files/%{up_name}-%{version}.tar.gz	
Patch:      extlib-1.5.1-install-flags.patch
BuildRequires:	ocaml
BuildRequires:  findlib
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

%prep
%setup -q -n %{up_name}-%{version}
%patch -p 1

%build
make 
make opt
make doc

%install
rm -rf %{buildroot}
install -d -m 755 %{buildroot}/%{ocaml_sitelib}
make install OCAMLFIND_INSTFLAGS="-destdir %{buildroot}/%{ocaml_sitelib}"

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README.txt LICENSE
%dir %{ocaml_sitelib}/extlib
%{ocaml_sitelib}/extlib/*.cmi

%files devel
%defattr(-,root,root)
%{ocaml_sitelib}/extlib/*
%exclude %{ocaml_sitelib}/extlib/*.cmi

