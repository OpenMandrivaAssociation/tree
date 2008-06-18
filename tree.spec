Name:           tree
Version:        1.5.1.1
Release:        %mkrel 2
Summary:        Utility which displays a tree view of directory contents
Group:          File tools
License:        GPL
URL:            http://mama.indstate.edu/users/ice/tree/
Source0:        ftp://mama.indstate.edu/linux/tree/%{name}-%{version}.tgz
Patch0:         %{name}-typo.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

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
%{make} RPM_OPT_FLAGS="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}/{%{_bindir},%{_sbindir},%{_mandir}/man1}

%{__make} \
        BINDIR=%{buildroot}%{_bindir} \
        MANDIR=%{buildroot}%{_mandir}/man1 \
        install

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README LICENSE CHANGES
%{_bindir}/%{name}
%{_mandir}/man1/%{name}*
