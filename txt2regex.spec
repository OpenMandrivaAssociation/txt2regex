%define name	txt2regex
%define version	0.8
%define release	%mkrel 4 

Summary:	A program to generate regex
Name:		%{name} 
Version:	%{version} 
Release:	%{release} 
Group:		File tools
License:	GPL
URL:		http://%{name}.sourceforge.net/ 
Source:		http://%{name}.sourceforge.net/%{name}-%{version}.tar.bz2
BuildArch:	noarch
Requires:	bash >= 2.04
BuildRoot:	%{_tmppath}/%{name}-buildroot 

%description
^txt2regex$ is a Regular Expression "wizard", all written 
with bash2 builtins, that converts human sentences to 
RegExs. with a simple interface, you just answer to 
questions and build your own RegEx for a large variety of 
programs, like awk, ed, emacs, grep, perl, php, procmail, 
python, sed and vim. there are more than 20 supported 
programs. it's bash so download and run, no compilation needed.

%prep 

%setup -q

%build 

%make DESTDIR=%{buildroot}

%install 
rm -rf %{buildroot}

%makeinstall_std

install -d %{buildroot}%{_mandir}/man1
install -m0644 txt2regex.man %{buildroot}%{_mandir}/man1/%{name}.1

%find_lang %{name}

%clean 
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root,0755) 
%doc README README.japanese NEWS Changelog TODO
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

