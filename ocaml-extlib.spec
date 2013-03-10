%define name	ocaml-extlib
%define up_name extlib
%define version	1.5.3
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
%doc README.txt LICENSE
%{_datadir}/doc/%{name}/*
%{_libdir}/ocaml/extlib/*.mli
%{_libdir}/ocaml/extlib/*.ml


%changelog
* Wed May 09 2012 Crispin Boylan <crisb@mandriva.org> 1.5.2-1
+ Revision: 797662
- New release

* Sat Jun 27 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.5.1-3mdv2011.0
+ Revision: 390042
- rebuild

* Sun Jan 18 2009 Florent Monnier <blue_prawn@mandriva.org> 1.5.1-2mdv2010.0
+ Revision: 330967
- added a doc package

* Wed Dec 24 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.5.1-2mdv2009.1
+ Revision: 318345
- move non-devel files in main package
- site-lib hierarchy doesn't exist anymore

* Wed Aug 13 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.5.1-1mdv2009.0
+ Revision: 271545
- import ocaml-extlib

