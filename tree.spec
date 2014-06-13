Summary:	Utility which displays a tree view of directory contents

Name:		tree
Version:	1.7.0
Release:	2
Group:		File tools
License:	GPLv2+
URL:		http://mama.indstate.edu/users/ice/tree/
Source0:	ftp://mama.indstate.edu:21/linux/tree/%{name}-%{version}.tgz
Patch1:         tree-1.5.2.2-link-flags.patch

%description
The tree utility recursively displays the contents of directories in a
tree-like format.  Tree is basically a UNIX port of the tree DOS
utility.

Install tree if you think it would be useful to view the contents of
specified directories in a tree-like format.

%prep

%setup -q
# %patch1 -p1 -b .linkflags

%build
%global optflags %{optflags} -Os
%serverbuild_hardened
%make CFLAGS="%{optflags} -Wall -DLINUX -D_LARGEFILE64_SOURCE -D_FILE_OFFSET_BITS=64" LDFLAGS="%{ldflags}"

%install

mkdir -p %{buildroot}/{%{_bindir},%{_sbindir},%{_mandir}/man1}

%makeinstall_std \
	BINDIR=%{buildroot}%{_bindir} \
	MANDIR=%{buildroot}%{_mandir}/man1

%files
%doc README LICENSE CHANGES
%{_bindir}/%{name}
%{_mandir}/man1/%{name}*



