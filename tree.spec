%define	name	tree
%define	version	1.5.1
%define	release %mkrel 1

Summary:	A utility which displays a tree view of directory contents
Name:		%{name}
Version:	%{version}
Release:	%{release}
Group:		File tools
License:	GPL
URL:		http://mama.indstate.edu/users/ice/tree/
Source0:	ftp://mama.indstate.edu/linux/tree/%{name}-%{version}.tar.bz2
Patch0:		%{name}-typopatch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
The tree utility recursively displays the contents of directories in a
tree-like format.  Tree is basically a UNIX port of the tree DOS
utility.

Install tree if you think it would be useful to view the contents of
specified directories in a tree-like format.

%prep
%setup -q
%patch0 -p1

%build
rm -f tree
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/{%{_bindir},%{_sbindir},%{_mandir}/man1}

make	BINDIR=$RPM_BUILD_ROOT%{_bindir} \
	MANDIR=$RPM_BUILD_ROOT%{_mandir}/man1 \
	install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/%{name}
%{_mandir}/man1/%{name}*
%doc README LICENSE CHANGES


