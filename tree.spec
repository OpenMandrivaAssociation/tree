Summary:	Utility which displays a tree view of directory contents
Name:		tree
Version:	1.6.0
Release:	1
Group:		File tools
License:	GPLv2+
URL:		http://mama.indstate.edu/users/ice/tree/
Source0:	ftp://mama.indstate.edu/linux/tree/%{name}-%{version}.tgz
Patch0:		tree-1.5.1.1-nostrip.diff

%description
The tree utility recursively displays the contents of directories in a
tree-like format.  Tree is basically a UNIX port of the tree DOS
utility.

Install tree if you think it would be useful to view the contents of
specified directories in a tree-like format.

%prep

%setup -q
%patch0 -p0 -b .nostrip

%build
make CFLAGS="%{optflags} -Wall -DLINUX -D_LARGEFILE64_SOURCE -D_FILE_OFFSET_BITS=64" LDFLAGS="%{ldflags}"

%install

%{__mkdir_p} %{buildroot}/{%{_bindir},%{_sbindir},%{_mandir}/man1}

%{__make} \
	BINDIR=%{buildroot}%{_bindir} \
	MANDIR=%{buildroot}%{_mandir}/man1 \
	install

%files
%doc README LICENSE CHANGES
%{_bindir}/%{name}
%{_mandir}/man1/%{name}*
